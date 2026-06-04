"""
unittest_run_all.py

This file retrieves the LLM's code attempts at solving the leetcode problems and unittest results for each attempt. Goal is to run the unittests, analyze and store the results, and perform analysis of the results with some additional graphical visualizations of the analysis. The analysis aims to show where the LLM has struggled the most and least to solve leetcode problems, and what metrics (difficulty, tags, constraints) have contributed to the result.

- Runs unit tests for all generated code for both C++ and Python, separately.
    - The results should be redirected to a file, python and cpp separately, for later evaluation.
        - Since python doesn't compile the code before running, we can directly run the tests and capture the results.
        - For C++, we need to compile the code first and then run the tests, capturing the results.
- Stores the results of each solution attempt in a structured JSON format for later evaluation for both C++ and Python, separately.
    - Each stored record should include the following information:
    - Leetcode Id
    - Result (pass/failed)
    - Error type if an (Syntax, Runtime, Logical/Assertion)
    - Difficulty
    - Number of examples provided
    - Number of constraints provided
    - etc

    Structure of each leetcode problem result stored in cpp/python json array
    ```json
    {
        "id": <leetcode_problem_id>,
        "difficulty": <difficulty of said leetcode problem>,
        "examples_count": <number examples given for said leetcode problem>,
        "constraints_count": <constraint rules given for each leetcode problem>,
        "tags": <list of tags/types of problems>,
        "attempts": [
            {
                "attempt_number": <attempt number>,
                "result": <pass or failure,
                "error_type": <Either no error, assertion error, or any syntax/runtime/import errors>,
                "raw_stderr": <raw output>
            },
        ],
        "total_attempts": <total attempts made to solve the problem>,
        "failed_attempts": <if attempts were failed, how many failed attempts>
        "passed_attempts": <if attempts were passed, how many passed attempts>
    },
    ```
    
    
- Evaluates the results of the tests and generates a summary or report of the results
    - Important list of analysis metrics
        -X Tag vs success rate
        -X Difficulty vs failure type
        -X Python vs C++ comparison
        -X First-attempt success rate
        - Failure progression analysis?
        - Constraint complexity correlation
        - Examples/constraints impact on correctness
    - The evaluation report should include metrics such as 
        - The number of tests passed, failed
        - Which failures were caused by Syntax, Runtime, or Logical/Assertion errors
        - What was the leetcode `difficulty` for each of the passed or failed test
        - What were the leetcode `tags` for each ofjthe the passed or failed test
        - How many leetcode `examples` were provided for each of the passed or failed test
        - How many leetcode `constraints` were provided for each of the passed or failed test
    - Creates graphs for each type of analysis
"""

import os
import json
import subprocess
import re
import shutil
from pathlib import Path
import time
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import argparse
import concurrent.futures
import shutil
import subprocess
import os
import json
from pathlib import Path
import re
import subprocess
from pathlib import Path
import json
from collections import defaultdict
import ast
import xml.etree.ElementTree as ET
from pathlib import Path
import seaborn as sns

# --- Constants ---
TIMEOUT_COMPILE = 60  # seconds
TIMEOUT_EXECUTE = 10  # seconds


PY_UNITTESTS_DIR = "python/"
CPP_UNITTESTS_DIR = "cpp/"

PY_UNITTEST_RESULTS_FILE = "python_test_results.json"
CPP_UNITTEST_RESULTS_FILE = "cpp_test_results.json"
FINAL_UNITTEST_RESULTS_FILE = "test_results.json"
GRAPH_OUTPUT_DIR = Path("analysis/figures")


TIMEOUT_ERROR = "Timeout Failure"
RUN_TIME_ERROR = "Runtime Error"
ASSERTION_FAILURE = "Assertion Failure"



# Order these keys in the order you want to check them (Highest priority first)
ERROR_MAPPINGS = {
    "Infrastructure/Build": [
r"make: \*\*\*", r"cmake error", r"permission denied", 
        r"no space left on device", r"fatal error: .* file not found"
    ],
    "Dependency/Definition": [
        r"unknown type name", 
        r"use of undeclared identifier", 
        r"no matching function", 
        r"undefined reference", 
        r"no member named", 
        r"ImportError", 
        r"ModuleNotFoundError",
        r"is not a member of",
        r"AttributeError" 
    ],
    "Syntax Error": [
        # Keep this list strictly about Grammar/Parsing
        r"SyntaxError", 
        r"IndentationError", 
        r"expected ';'", 
        r"expected '\)'", 
        r"unbalanced parenthesis",
        r"expected '\}'",
        r"expected expression" # Added back here, but only after Dependency is checked
    ],
    "Memory/Pointer": [
        r"MemoryError", r"RecursionError", r"Segmentation fault", 
r"std::bad_alloc", r"free\(\)", r"heap-use-after-free"
],
    "Logic/Boundary": [
r"IndexError", r"KeyError", r"TypeError", r"NameError", 
        r"std::out_of_range", r"out of bounds"
    ],
    "Assertion Failure": [
r"Failure", r"FAILED", r"Expected equality", r"Value of:", 
        r"Assertion `.*' failed", r"AssertionError"
    ],
    "Arithmetic": [
        r"ZeroDivisionError", r"Floating point exception", r"divide by zero"
    ],
}
ERROR_PRIORITY_ORDER = [
    "Memory/Pointer",     # Includes RecursionError, Segfault
    "Syntax Error",
    "Dependency/Definition",
    "Infrastructure/Build",
    "Logic/Boundary",
    "Arithmetic",
    "Assertion Failure"   # Symptom, not root cause
]

def get_unified_error_type(output: str, returncode: int = 0) -> str:
    if not output:
        return "Unknown/Logical Failure"

    # 1. PRIORITY: System Crashes (Signal based - Hard check)
    if returncode < 0:
        return "Runtime Crash (Signal)"

    # 2. PRIORITY: Root Cause Analysis (Waterfall)
    # We loop through our defined priority list
    for category in ERROR_PRIORITY_ORDER:
        patterns = ERROR_MAPPINGS.get(category, [])
        for pattern in patterns:
            # We use re.IGNORECASE to ensure we catch 'recursionerror' and 'RecursionError'
            if re.search(pattern, output, re.IGNORECASE | re.DOTALL):
                return category
    
    return "Unknown/Logical Failure"

def get_lines_of_code(file_path: str) -> int:
    """
# Tags and their corresponding problem ids for later analysis and visualization
DISTRIBUTED_TAGS = [ "Array", "String", "Linked List", "Heap (Priority Queue)", "Binary Tree" ]
    Counts the number of non-empty lines in a file.
    Works for any text-based source code file (.py, .cpp, .h, etc.)
    """
    if not os.path.exists(file_path):
        return 0
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            # We filter out blank lines and whitespace-only lines 
            # to get a more accurate measure of 'code' density.
            lines = [line for line in f if line.strip()]
            return len(lines)
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
        return 0

# Tags and their corresponding problem ids for later analysis and visualization
DISTRIBUTED_TAGS = [ "Array", "String", "Linked List", "Binary Tree", "Heap (Priority Queue)"]
def insert_distributed_tags_into_library():
    """
    Inserts distributed tags into the leetcode_library.json file.
    """

    file_path = "../problem_extraction/leetcode_library.json"
    try:
        # 1. READ: Open in 'r' mode to get the data
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        # 2. MODIFY: Loop through data
        for i, entry in enumerate(data):
            # Calculate tag index: 
            # (i // 4) moves to the next tag every 4 entries
            # % len(...) ensures it wraps back to 0 when it reaches the end of the list
            tag_index = (i // 4) % len(DISTRIBUTED_TAGS)
            entry["distributed_tag"] = DISTRIBUTED_TAGS[tag_index]

        # 3. WRITE: Open in 'w' mode to save the updated data
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
            
        print(f"Successfully processed {len(data)} entries in {file_path}")
        
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check your file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Helper to load library metadata
def get_metadata(problem_id):
    # Adjust this path to your actual leetcode_library.json
    try:
        with open("../problem_extraction/leetcode_library.json", "r") as f:
            data = json.load(f)
            for entry in data:
                if str(entry.get("id")) == str(problem_id):
                    return entry
    except:
        return {"difficulty": "Unknown", "tags": [], "examples": [], "constraints": []}
    return {"difficulty": "Unknown", "tags": [], "examples": [], "constraints": []}

def parse_gtest_metrics(stdout: str, xml_path: Path):
    """
    Consolidated helper to get metrics.
    Prioritizes stdout, falls back to XML.
    Returns (total_tests, passed_tests)
    """
    # 1. Try Stdout (Primary)
    total_match = re.search(r"\[==========\] (\d+) tests from", stdout)
    passed_match = re.search(r"\[\s+PASSED\s+\] (\d+) tests", stdout)
    
    total = int(total_match.group(1)) if total_match else 0
    passed = int(passed_match.group(1)) if passed_match else 0
    
    if total > 0:
        return total, passed

    # 2. Fallback to XML (Secondary)
    if xml_path.exists():
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            # Sum up from all testsuites
            t, p = 0, 0
            for ts in root.findall('.//testsuite'):
                t += int(ts.attrib.get('tests', 0))
                # passed = tests - (failures + errors)
                f = int(ts.attrib.get('failures', 0))
                e = int(ts.attrib.get('errors', 0))
                p += (int(ts.attrib.get('tests', 0)) - (f + e))
            return t, p
        except Exception:
            print("Error parsing XML report:", xml_path)
            pass
            
    return 0, 0

def run_single_task(sol_file, source_dir, base_build_dir):
    # 1. Reliable metadata extraction
    match = re.search(r"solution_(\d+)_(\d+)", sol_file.name)
    if not match:
        return {"error": f"Invalid filename format: {sol_file.name}"}
    
    prob_id, attempt_num = match.group(1), int(match.group(2))
    work_dir = base_build_dir / f"work_{sol_file.stem}"
    work_dir.mkdir(exist_ok=True, parents=True)
    
    # 3. Create proxy header
    proxy_header = work_dir / "solution_proxy.h"
    with open(proxy_header, "w") as f:
        f.write(f'#include "{sol_file.resolve()}"')
    
    # 4. Configure
    if not (work_dir / "CMakeCache.txt").exists():
        subprocess.run(["cmake", "-S", str(source_dir), "-B", str(work_dir)], capture_output=True)

    # 5. Build
    binary_name = f"run_test_unittest_{prob_id}"
    build_result = subprocess.run(
        ["cmake", "--build", str(work_dir), "--target", binary_name], 
        capture_output=True, text=True, timeout=TIMEOUT_COMPILE
    )

    loc = get_lines_of_code(sol_file)

    if build_result.returncode != 0:
        return {
            "prob_id": prob_id,
            "attempt_num": attempt_num,
            "has_compiled": False,
            "result": "failed",
            "total_tests": 0,
            "passed_tests": 0,
            "loc": loc,
            "error_type": get_unified_error_type(build_result.stderr, build_result.returncode),
            "raw_stdout": build_result.stdout,
            "raw_stderr": build_result.stderr
        }

    # 6. Execution and Triage Logic
    binary_path = work_dir / binary_name
    xml_report = work_dir / "report.xml"
    
    result, stderr_output, stdout_output = "failed", "", ""
    total_tests, passed_tests = 0, 0
    has_compiled = True
    
    # Run the test
    cmd = [str(binary_path), f"--gtest_output=xml:{xml_report}"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_EXECUTE)
        
        stderr_output = proc.stderr
        stdout_output = proc.stdout
        combined_output = f"{proc.stdout}\n{proc.stderr}"
        
        # Clean, singular point of truth for metrics
        total_tests, passed_tests = parse_gtest_metrics(combined_output, xml_report)
        
        error_type = -1
        if proc.returncode == 0:
            result = "pass"
            error_type = "None"
        else:
            result = "failed"
            error_type = get_unified_error_type(combined_output, proc.returncode)
    except subprocess.TimeoutExpired as e:
        result, error_type = "failed", "Timeout"
        stderr_output = "Execution timed out"

    return {
        "prob_id": prob_id,
        "attempt_num": attempt_num,
        "has_compiled": has_compiled,
        "result": result,
        "loc": loc,
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "error_type": error_type,
        "raw_stdout": stderr_output,
        "raw_stderr": stdout_output
    }

def run_parallel_tests(unittest_files_dir: str):
    source_dir = Path(unittest_files_dir)
    base_build_dir = source_dir / "builds_parallel"
    base_build_dir.mkdir(exist_ok=True)
    
    solution_files = list(source_dir.glob("solution_*.cpp"))
    
    # Parallel processing
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run_single_task, f, source_dir, base_build_dir) for f in solution_files]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
            results_num = len(results)
            #if results_num % 30 or results_num == 1:
            print(f"Added {len(results)}/{len(solution_files)} results")
            
    # Cleanup: remove the workspace folder after task is done
    # shutil.rmtree(base_build_dir) # Optional: uncomment if you want to clear after run
    return results

def aggregate_and_save(results, output_file_path):
    # Using defaultdict simplifies the initialization of the nested structure
    # Structure: problem_map[prob_id] = { ... }
    problem_map = {}

    for res in results:
        prob_id = res["prob_id"]
        
        # Initialize entry if new
        if prob_id not in problem_map:
            meta = get_metadata(prob_id) # Ensure this is thread-safe or cached
            problem_map[prob_id] = {
                "id": prob_id,
                "attempts": [],
                #"total_assertions": res["total_assertions"],
                "total_tests": 0,
                "passed_attempts": 0,
                "failed_attempts": 0
            }
        
        # Update attempt stats
        problem_map[prob_id]["attempts"].append({
            "attempt_number": res["attempt_num"],
            "has_compiled": res["has_compiled"],
            "loc": res["loc"],
            "result": res["result"],
            "passed_tests": res["passed_tests"],
            "error_type": res["error_type"],
            "raw_stdout": res["raw_stdout"],
            "raw_stderr": res["raw_stderr"]
        })
        
        # 1. Update total_tests with the MAX observed (The "High-Water Mark")
        problem_map[prob_id]["total_tests"] = max(
            problem_map[prob_id]["total_tests"], 
            res["total_tests"]
        )
        if res["result"] == "pass":
            problem_map[prob_id]["passed_attempts"] += 1
        else:
            problem_map[prob_id]["failed_attempts"] += 1
            
        # Finalize total
        problem_map[prob_id]["total_attempts"] = len(problem_map[prob_id]["attempts"])

    # Sorting before saving makes the JSON file readable and deterministic
    sorted_results = sorted(problem_map.values(), key=lambda x: x["id"])

    # Save to JSON
    with open(output_file_path, "w") as f:
        json.dump(list(problem_map.values()), f, indent=4)
        
    print(f"Successfully saved {len(problem_map)} problem results to {output_file_path}")

    return len(problem_map)

def analyze_test_file(file_path):
    """
    Statically analyzes the test file to count total test methods 
    and total assertions, without running the code.
    """
    with open(file_path, "r") as source:
        tree = ast.parse(source.read())
    
    total_tests = 0
    total_assertions = 0
    
    for node in ast.walk(tree):
        # 1. Count Methods starting with 'test_'
        if isinstance(node, ast.FunctionDef):
            if node.name.startswith('test_'):
                total_tests += 1
        
        # 2. Count Assertion calls
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if node.func.attr.startswith('assert'):
                    total_assertions += 1
            elif isinstance(node.func, ast.Name):
                if node.func.id == 'assert':
                    total_assertions += 1
                    
    return total_tests, total_assertions

def get_passed_test_count(stderr_output, total_tests):
    """
    Parses unittest output (e.g., 'Ran 4 tests... FAILED (failures=1)')
    """
    # Find number of failures and errors
    failures = re.search(r"failures=(\d+)", stderr_output)
    errors = re.search(r"errors=(\d+)", stderr_output)
    
    num_failures = int(failures.group(1)) if failures else 0
    num_errors = int(errors.group(1)) if errors else 0
    
    return total_tests - (num_failures + num_errors)

def run_and_store_python_tests(unittest_files_dir: str, output_file_path: str) -> int:
    """
    Discovers and runs Python unit tests for all generated code.

    This function should be implemented to find and execute Python unit tests,
    and store the results in a structured format (e.g., JSON, XML).

    Args:
        unittest_files_dir (str): The directory where Python unit test files are located.
        output_file_path (str): The file path where the test results should be stored.
    Returns:
        int: The number of tests that were added to the results.
    """
    problem_map = {}
    tests_added = 0
    solution_files = sorted(Path(unittest_files_dir).glob("solution_*.py"))

    for sol_file in solution_files:
        match = re.search(r"solution_(\d+)_(\d+)", sol_file.name)
        if not match: continue
        prob_id, attempt_num = match.group(1), match.group(2)
        
        test_file = Path(unittest_files_dir) / f"test_unittest_{prob_id}.py"
        
        # Get Static Assertion Count (Done once per problem)
        if prob_id not in problem_map:
            meta = get_metadata(prob_id)
            total_tests, total_assertions = analyze_test_file(test_file)
            # 4. Store
            problem_map[prob_id] = {
                "id": prob_id,
                "total_tests": total_tests,
                "total_assertions": total_assertions, # Added requirement
                "total_attempts": 0,
                "attempts": []
            }

        #  Execution
        env = os.environ.copy()
        env["TEST_SOLUTION_FILE"] = str(sol_file.absolute())
        cmd = ["python3", "-m", "unittest", str(test_file)]
        

        # 2. Run test
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env)

        # 3. Calculate metrics
        if proc.returncode == 0:
            passed_tests = total_tests
            error_type = "None"
        else:
            passed_tests = get_passed_test_count(proc.stderr, total_tests)
            error_type = get_unified_error_type(proc.stderr, proc.returncode)

        loc = get_lines_of_code(sol_file)

        attempt_data = {
            "attempt_number": int(attempt_num),
            "result": "pass" if proc.returncode == 0 else "failed",
            "passed_tests": passed_tests, # Renamed as requested
            "loc": loc, 
            "error_type": error_type,
            "raw_stderr": proc.stderr if proc.returncode != 0 else ""
        }
        problem_map[prob_id]["attempts"].append(attempt_data)
        total_attempts = len(problem_map[prob_id]["attempts"])
        attempt_result = attempt_data["result"]

        #print('Running on problem ID:', prob_id, 'Attempt:', attempt_num, 'Result:', attempt_result)
        problem_map[prob_id]["total_attempts"] = total_attempts
        if attempt_result == "failed":
            if "failed_attempts" not in problem_map[prob_id]:
                problem_map[prob_id]["failed_attempts"] = 1
            else:
                problem_map[prob_id]["failed_attempts"] += 1
        elif attempt_result == "pass":
            if "passed_attempts" not in problem_map[prob_id]:
                problem_map[prob_id]["passed_attempts"] = 1
            else:
                problem_map[prob_id]["passed_attempts"] += 1

        tests_added += 1

    # 7. Convert map back to list for final JSON output
    with open(output_file_path, "w") as f:
        json.dump(list(problem_map.values()), f, indent=4)

    return tests_added

def merge_test_results(python_results_source: str, cpp_results_source) -> int:
    """
    Merges the results of cpp and python unittest runs on each leetcode problem into a single file

    Args:
        python_results_source (str): file path to the python unittest results
        cpp_results_source (str): file path to the cpp unittest results 
    
    Returns: 
        The amount of records stored in the final results file `FINAL_UNITTEST_RESULTS_FILE`
    """
    python_results = None
    cpp_results = None
    with open(python_results_source, "r") as f:
        python_results = json.load(f)

    with open(cpp_results_source, "r") as f:
        cpp_results = json.load(f)

    # -----------------------------
    # Merge each problem
    # -----------------------------

    python_by_id = {
        record["id"]: record
        for record in python_results
    }

    cpp_by_id = {
        record["id"]: record
        for record in cpp_results
    }

    # -----------------------------
    # Union of all problem ids
    # -----------------------------

    all_problem_ids = set(python_by_id.keys()) | set(cpp_by_id.keys())

    merged_results = []

    # -----------------------------
    # Merge each problem
    # -----------------------------

    for problem_id in sorted(all_problem_ids):

        py_record = python_by_id.get(problem_id)
        cpp_record = cpp_by_id.get(problem_id)

        # Use whichever exists for metadata
        metadata_source = get_metadata(problem_id=problem_id)

        merged_entry = {
            "id": problem_id,
            "difficulty": metadata_source.get("difficulty"),
            "examples_count": len(metadata_source.get("examples")),
            "constraints_count": len(metadata_source.get("constraints")),
            "distributed_tag": metadata_source.get("distributed_tag", "Unknown"),
            "tags": metadata_source.get("tags", []),

            "python": {
                "attempts": [],
                "total_tests": 0,
                #"total_assertions": 0,
                "total_attempts": 0,
                "passed_attempts": 0,
                "failed_attempts": 0
            },

            "cpp": {
                "attempts": [],
                "total_tests": 0,
                #"total_assertions": 0,
                "total_attempts": 0,
                "passed_attempts": 0,
                "failed_attempts": 0
            }
        }

        # -----------------------------
        # Insert python results
        # -----------------------------

        if py_record:

            merged_entry["python"] = {
                "attempts": py_record.get("attempts", []),
                "total_tests": py_record.get("total_tests", 0),
                "total_attempts": py_record.get("total_attempts", 0),
                "passed_attempts": py_record.get("passed_attempts", 0),
                "failed_attempts": py_record.get("failed_attempts", 0)
            }

        # -----------------------------
        # Insert cpp results
        # -----------------------------

        if cpp_record:

            merged_entry["cpp"] = {
                "attempts": cpp_record.get("attempts", []),
                "total_tests": cpp_record.get("total_tests", 0),
                "total_attempts": cpp_record.get("total_attempts", 0),
                "passed_attempts": cpp_record.get("passed_attempts", 0),
                "failed_attempts": cpp_record.get("failed_attempts", 0)
            }

        merged_results.append(merged_entry)

    # -----------------------------
    # Save final merged dataset
    # -----------------------------

    with open(FINAL_UNITTEST_RESULTS_FILE, "w") as f:
        json.dump(merged_results, f, indent=4)

    return merged_results

def generate_attempts_dataframe(merged_results: list) -> pd.DataFrame:
    attempt_rows = []

    for problem in merged_results:
        for language in ["python", "cpp"]:
            lang_data = problem.get(language, {})
            # Ensure we are looking at a sorted list of attempts
            attempts = sorted(lang_data.get("attempts", []), key=lambda x: x.get("attempt_number", 0))
                        
            for attempt in attempts:
                attempt_rows.append({
                    "id": problem["id"],
                    "language": language,
                    "difficulty": problem["difficulty"],
                    "examples_count": problem["examples_count"],
                    "constraints_count": problem["constraints_count"],
                    # Keep tags as a list or join to a string, DO NOT EXPLODE YET
                    "distributed_tag": problem.get("distributed_tag", "Unknown"),
                    "tags": problem["tags"], 
                    "attempt_number": attempt["attempt_number"],
                    "result": attempt["result"],
                    "error_type": attempt["error_type"],
                    "total_tests": lang_data.get("total_tests", 0), 
                    "passed_tests": attempt.get("passed_tests", 0),
                    "loc": attempt.get("loc", 0)
                })

    # No .explode() here!
    attempt_df = pd.DataFrame(attempt_rows)
    attempt_df.attrs['name'] = 'Leetcode Attempts Results'
    return attempt_df

def generate_problem_dataframe(merged_results: list) -> pd.DataFrame:
    problem_rows = []

    for problem in merged_results:
        for language in ["python", "cpp"]:
            lang_data = problem.get(language, {})
            attempts = sorted(lang_data.get("attempts", []), key=lambda x: x.get("attempt_number", 0))

            # Integrity Check
            passed_count_from_list = sum(1 for a in attempts if a.get("result") == "pass")
            stored_passed_count = lang_data.get("passed_attempts", 0)

            if passed_count_from_list != stored_passed_count:
                print(f"Warning: Integrity Mismatch on ID {problem['id']} ({language}). "
                      f"Calculated: {passed_count_from_list}, Stored: {stored_passed_count}")

            # Define First Try Success: Must exist, be attempt 1, and pass
            first_try_success = False
            if attempts:
                first_attempt = attempts[0]
                if first_attempt.get("attempt_number") == 1 and first_attempt.get("result") == "pass":
                    first_try_success = True

            problem_rows.append({
                "id": problem["id"],
                "language": language,
                "difficulty": problem["difficulty"],
                "examples_count": problem["examples_count"],
                "constraints_count": problem["constraints_count"],
                "distributed_tag": problem.get("distributed_tag", "Unknown"),
                "tags": problem["tags"], # Keep as list
                "eventually_passed": stored_passed_count > 0,
                "first_try_success": first_try_success,
                "total_attempts": lang_data.get("total_attempts", 0),
                "passed_attempts": stored_passed_count,
                "failed_attempts": lang_data.get("failed_attempts", 0),
                "total_tests": lang_data.get("total_tests", 0)
            })

    problems_df = pd.DataFrame(problem_rows)
    problems_df.attrs['name'] = 'Leetcode Problems Results'
    return problems_df

def generate_comparison_summary(attempt_df: pd.DataFrame, problems_df: pd.DataFrame, output_file="summary_comparison.csv"): 
    """
    Creates a summary table to audit data quality and performance metrics.
    """
    # 1. Clean the data for the audit (Remove suspected duplicates if needed)
    # Check for duplicates before aggregating
    # print(f"Total rows in attempt_df: {len(attempt_df)}")
    print(f"Duplicates detected: {attempt_df.duplicated().sum()}")

    # Use a working copy
    df = attempt_df.copy()

    # 2. Build the Comparison Table
    summary = df.groupby('language').agg(
        total_attempts=('id', 'count'),
        unique_problems=('id', 'nunique'),
        avg_loc=('loc', 'mean'),
        pass_rate=('result', lambda x: (x == 'passed').mean()),
        fail_rate=('result', lambda x: (x == 'failed').mean())
    )

    # 3. Add Problem-level metadata (optional, requires merge)
    # This helps confirm if the number of problems matches your expected 180
    prob_summary = problems_df.groupby('language').agg(
        total_problems_in_catalog=('id', 'nunique'),
        avg_eventually_passed=('eventually_passed', 'mean')
    )

    # Merge and format
    final_summary = pd.concat([summary, prob_summary], axis=1)

    # 4. Save to File
    final_summary.to_csv(output_file)
    print(f"\n--- Summary Table Saved to {output_file} ---")
    print(final_summary)
    return final_summary

# --------------------------------------------------
# Individual Plotting Functions
# --------------------------------------------------

def save_current_figure(filename: str) -> None:
    """Saves the current matplotlib figure and closes it."""
    GRAPH_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(GRAPH_OUTPUT_DIR / filename)
    plt.close()

def plot_graph_difficulty_distribution(attempt_df: pd.DataFrame):
    """
    Measures the frequency of 'Easy', 'Medium', and 'Hard' attempts.
    """
    plt.figure(figsize=(8, 6))
    
    # We define the order explicitly so the x-axis logic follows difficulty level,
    # rather than just alphabetical order.
    difficulty_order = ['Easy', 'Medium', 'Hard']
    
    sns.countplot(
        data=attempt_df, 
        x='difficulty', 
        order=difficulty_order,
        palette='viridis',
        edgecolor='black'
    )
    
    plt.title("Distribution of Attempt Difficulty")
    plt.xlabel("Difficulty Level")
    plt.ylabel("Number of Attempts")
    
    save_current_figure("graph_difficulty_distribution.png")

def plot_graph_distributed_tag_distribution(attempt_df: pd.DataFrame):
    """
    Measures how often each 'distributed_tag' appears in your attempts.
    """
    plt.figure(figsize=(10, 6))
    
    # Using a countplot to see if the tag distribution is balanced
    sns.countplot(
        data=attempt_df, 
        x='distributed_tag', 
        palette='magma',
        edgecolor='black'
    )
    
    plt.title("Distribution of Attempts by Distributed Tag")
    plt.xlabel("Tag Category")
    plt.ylabel("Number of Attempts")
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    save_current_figure("graph_distributed_tag_distribution.png")

# Bar Graph: Measure # of failed attempts in C++ vs Python
def plot_graph_failed_attempts(attempt_df: pd.DataFrame):
    failures = attempt_df[attempt_df['result'] == 'failed']
    plt.figure(figsize=(8, 6))
    sns.countplot(data=failures, x='language', palette='viridis')
    plt.title("Total Failed Attempts by Language")
    plt.xticks(rotation=0)
    save_current_figure("graph_failed_attempts.png")

# a. HEATMAP: Measure # of failed attempts vs passed attempts in C++ vs Python
def plot_graph_a_failed_vs_passed(attempt_df: pd.DataFrame):
    # 1. Update these to match your actual data (e.g., 'pass', 'failed')
    # Use the print statement above to confirm the exact spelling
    valid_results = ['pass', 'failed']

    # 2. Filter
    df_clean = attempt_df[attempt_df['result'].isin(valid_results)].copy()
    
    # 3. Use countplot (it's cleaner for binary comparison)
    plt.figure(figsize=(8, 6))
    sns.countplot(
        data=df_clean, 
        x='language', 
        hue='result', 
        palette={'pass': 'green', 'failed': 'red'}
    )
    
    plt.title("Performance: Pass vs. Fail Count by Language")
    plt.ylabel("Number of Attempts")
    plt.xticks(rotation=0)

    save_current_figure("graph_a_failed_vs_passed.png")

# b. HEATMAP: Measure # of failed attempts vs difficulty type in C++ vs Python
def plot_graph_b_failed_vs_difficulty(attempt_df: pd.DataFrame):
    failures = attempt_df[attempt_df['result'] == 'failed']
    matrix = failures.pivot_table(index='difficulty', columns='language', aggfunc='size', fill_value=0)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds', cbar_kws={'label': 'Failed Count'})
    plt.title("Failures by Difficulty & Language")
    plt.xticks(rotation=0)
    save_current_figure("graph_b_failed_vs_difficulty.png")

# bc. HEATMAP: Measure # of failures vs difficulty type vs error type in C++ vs Python
def plot_graph_bc_failures_difficulty_error(attempt_df: pd.DataFrame):
    failures = attempt_df[attempt_df['result'] == 'failed']
    # Create multi-index pivot
    matrix = failures.pivot_table(
        index=['difficulty', 'error_type'], 
        columns='language', 
        aggfunc='size', 
        fill_value=0
    )
    plt.figure(figsize=(10, 10))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Purples', cbar_kws={'label': 'Failed Count'})
    plt.title("Failures: Difficulty & Error Type by Language")
    plt.xticks(rotation=0)
    save_current_figure("graph_bc_failures_difficulty_error.png")

# c. HEATMAP: Measure # of failed attempts vs error type in C++ vs Python
def plot_graph_c_failed_vs_error_type(attempt_df: pd.DataFrame):
    failures = attempt_df[attempt_df['result'] == 'failed']
    matrix = failures.pivot_table(index='error_type', columns='language', aggfunc='size', fill_value=0)
    plt.figure(figsize=(8, 8))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Failed Count'})
    plt.title("Failed Attempts by Error Type")
    plt.xticks(rotation=0)
    save_current_figure("graph_c_failed_vs_error_type.png")

# d. HEATMAP: Measure # of failed attempts vs distributed tag type in C++ vs Python
def plot_graph_d_failed_vs_tag_language(attempt_df: pd.DataFrame):
    """
    Measures the # of failed attempts, segmented by distributed_tag and language.
    """
    # 1. Filter for only failed attempts
    df_fails = attempt_df[attempt_df['result'] == 'failed'].copy()
    
    # 2. Pivot the data to create a matrix
    # Index = Tag, Columns = Language
    matrix = df_fails.groupby(['distributed_tag', 'language']).size().unstack(fill_value=0)
    
    # 3. Create Heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        matrix, 
        annot=True,      # Show the actual numbers
        fmt='d',         # Integer formatting
        cmap='Reds',     # Red intensity represents failure count
        cbar_kws={'label': 'Number of Failed Attempts'}
    )
    
    plt.title("Failure Frequency: Distributed Tag vs. Language")
    plt.xlabel("Programming Language")
    plt.ylabel("Distributed Tag")
    plt.yticks(rotation=0)
    
    plt.tight_layout()
    save_current_figure("graph_d_failed_vs_tag_language.png")

import seaborn as sns
import matplotlib.pyplot as plt

def plot_graph_failure_pinpoint_matrix(attempt_df: pd.DataFrame):
    """
    Creates a multi-dimensional matrix to pinpoint specific causes of failures.
    Rows: Error Type
    Cols: Distributed Tag
    X-Axis: Difficulty
    Hue: Language
    """
    # 1. Filter only failures
    failures = attempt_df[attempt_df['result'] == 'failed'].copy()
    
    # 2. Create the Faceted Catplot
    # We use sharey=False because error counts will vary wildly (e.g., Syntax errors 
    # are usually more common than Memory errors)
    g = sns.catplot(
        data=failures,
        x='difficulty',
        hue='language',
        col='distributed_tag',
        row='error_type',
        kind='count',
        order=['Easy', 'Medium', 'Hard'],
        palette={'python': 'blue', 'cpp': 'red'},
        height=3, 
        aspect=1.2,
        sharey=False, 
        edgecolor='black'
    )
    
    # 3. Formatting
    g.set_titles("{row_name} | {col_name}")
    g.set_axis_labels("Difficulty", "Failure Count")
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle('Failure Pinpoint Matrix: Error Type vs Tag vs Difficulty vs Language')
    
    save_current_figure("graph_failure_pinpoint_matrix.png")



# HEATMAP: Failed attempts vs Lines of Code (LOC)
def plot_graph_failed_vs_loc(attempt_df: pd.DataFrame):
    """
    Measures # of failed attempts vs binned Lines of Code.
    """
    failures = attempt_df[attempt_df['result'] == 'failed'].copy()
    
    # Create LOC bins (0-50, 50-100, 100-200, etc.)
    # You can adjust these bins based on your specific codebase size
    bins = [0, 50, 100, 200, 500, 1000, 5000]
    labels = ['0-50', '51-100', '101-200', '201-500', '501-1000', '1000+']
    failures['loc_bin'] = pd.cut(failures['loc'], bins=bins, labels=labels)
    
    # Pivot for Heatmap
    matrix = failures.pivot_table(index='loc_bin', columns='language', aggfunc='size', fill_value=0)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='OrRd', cbar_kws={'label': 'Failed Count'})
    plt.title("Failed Attempts by Lines of Code (LOC)")
    plt.ylabel("LOC Range")
    plt.xticks(rotation=0)
    save_current_figure("graph_failed_vs_loc.png")

# HEATMAP: Failed attempts vs Number of Tags
def plot_graph_failed_vs_tags(attempt_df: pd.DataFrame):
    """
    Measures # of failed attempts vs the number of tags assigned to the problem.
    """
    failures = attempt_df[attempt_df['result'] == 'failed'].copy()
    
    # Count the number of tags (assuming 'tags' is a list)
    failures['tag_count'] = failures['tags'].apply(lambda x: len(x) if isinstance(x, list) else 0)
    
    # Pivot for Heatmap
    matrix = failures.pivot_table(index='tag_count', columns='language', aggfunc='size', fill_value=0)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='PuBu', cbar_kws={'label': 'Failed Count'})
    plt.title("Failed Attempts by Number of Tags")
    plt.ylabel("Number of Tags")
    plt.xticks(rotation=0)
    save_current_figure("graph_failed_vs_tags.png")

# Your precedence list
TAG_PRECEDENCE = ['String', 'Array', 'Linked List', 'Binary Tree', 'Heap (Priority Queue)']

# --------------------------------------------------
# Main Orchestrator
# --------------------------------------------------

def plot_graph_difficulty_by_tag(attempt_df: pd.DataFrame):
    """
    Measures the distribution of Difficulty levels, grouped by the Distributed Tag.
    """
    plt.figure(figsize=(12, 7))
    
    # 1. Define specific orders to ensure logical reading
    difficulty_order = ['Easy', 'Medium', 'Hard']
    
    # 2. Use countplot with 'hue' to group by difficulty
    sns.countplot(
        data=attempt_df, 
        x='distributed_tag', 
        hue='difficulty', 
        hue_order=difficulty_order,
        palette={'Easy': 'green', 'Medium': 'orange', 'Hard': 'red'},
        edgecolor='black'
    )
    
    plt.title("Attempt Distribution: Difficulty Levels per Distributed Tag")
    plt.xlabel("Distributed Tag Category")
    plt.ylabel("Number of Attempts")
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Difficulty')
    
    plt.tight_layout()
    save_current_figure("graph_difficulty_by_tag.png")

def generate_graph_report(attempt_df, problems_df):
    """
    Categorized execution of all plotting functions.
    """

    # Prove the dataframe distribution are correct
    plot_graph_difficulty_distribution(attempt_df)
    plot_graph_distributed_tag_distribution(attempt_df)
    plot_graph_difficulty_by_tag(attempt_df)
    
    plot_graph_failed_attempts(attempt_df)

    # Primary analysis
    plot_graph_a_failed_vs_passed(attempt_df)
    plot_graph_b_failed_vs_difficulty(attempt_df)
    plot_graph_c_failed_vs_error_type(attempt_df)
    plot_graph_d_failed_vs_tag_language(attempt_df)

    # Zoomed in
    plot_graph_bc_failures_difficulty_error(attempt_df)

    # Complete zoom in
    plot_graph_failure_pinpoint_matrix(attempt_df)


    plot_graph_failed_vs_loc(attempt_df)
    plot_graph_failed_vs_tags(attempt_df)

    print(f"All reports saved to: {GRAPH_OUTPUT_DIR}")

def run_and_store_unittests_separately() -> int:
    """
    Returns:
        int: results of cpp and python tests stored separate files
    """
    print("Running C++ unit tests...")
    all_results = run_parallel_tests(CPP_UNITTESTS_DIR)
    print(f"Added {len(all_results)} C++ tests to results. Not yet saved to the file")
    # 2. Aggregate and save
    tests_added_cpp = aggregate_and_save(all_results, CPP_UNITTEST_RESULTS_FILE)
    print(f"Added {tests_added_cpp} C++ tests to results.")

    print("Running Python unit tests...")
    tests_added_py = run_and_store_python_tests(PY_UNITTESTS_DIR, PY_UNITTEST_RESULTS_FILE)
    print(f"Added {tests_added_py} Python tests to results.")

    return tests_added_cpp + tests_added_py

def print_dataframe(df, first_rows):
    dashes = "-"*5
    print(f"\n\n{dashes} {df.attrs['name']}\n")
    print(df.head(first_rows))
    print("Columns: ", df.columns.tolist())
    print(f"\n\n{dashes}")

def main():
    """
    Main function to run all unit tests for generated code.
    """

    parser = argparse.ArgumentParser(description="Cherry pick specific functionality")
    # 4. Define an optional boolean flag to not run cpp and python unittests (True if present, False if absent)
    parser.add_argument("-a", "--analysis_only", action="store_true", help="Skip creation of unittest results to start analysis")
    args = parser.parse_args()

    insert_distributed_tags_into_library()
 
    if args.analysis_only:
        print("Skipping to analysis...")
    else:
        tests_added_total = run_and_store_unittests_separately()
        print(f"Added {tests_added_total} tests in total")

    print("Merging C++ and Python unit test results...")
    merged_results: list = merge_test_results(python_results_source=PY_UNITTEST_RESULTS_FILE, 
    cpp_results_source=CPP_UNITTEST_RESULTS_FILE)
    print(f"Merged {len(merged_results)} tests in total.")

    print("Converting attempts into the dataframe...")
    attempts_df = generate_attempts_dataframe(merged_results)
    print(f"Created attempt dataframe with {len(attempts_df)} rows")

    print("Converting problems into the dataframe...")
    problems_df = generate_problem_dataframe(merged_results)
    print(f"Created problem dataframe with {len(problems_df)} rows")

    print_dataframe(attempts_df, 10)
    print_dataframe(problems_df, 10)

    print("generating validation tables..")

    generate_graph_report(attempts_df, problems_df)
    print("Summary report generated.")

if __name__ == "__main__":
    main()