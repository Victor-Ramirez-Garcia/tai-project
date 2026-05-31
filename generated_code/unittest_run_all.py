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


PY_UNITTESTS_DIR = "python/"
CPP_UNITTESTS_DIR = "cpp/"

PY_UNITTEST_RESULTS_FILE = "python_test_results.json"
CPP_UNITTEST_RESULTS_FILE = "cpp_test_results.json"
FINAL_UNITTEST_RESULTS_FILE = "test_results.json"
GRAPH_OUTPUT_DIR = Path("analysis/figures")

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

import concurrent.futures
import shutil
import subprocess
import os
import json
from pathlib import Path

# --- Constants ---
TIMEOUT_COMPILE = 60  # seconds
TIMEOUT_EXECUTE = 10  # seconds
import re
import subprocess
from pathlib import Path

def run_single_task(sol_file, source_dir, base_build_dir):
    # 1. Reliable metadata extraction
    match = re.search(r"solution_(\d+)_(\d+)", sol_file.name)
    if not match:
        return {"error": f"Invalid filename format: {sol_file.name}"}
    
    prob_id, attempt_num = match.group(1), int(match.group(2))
    
    # 2. Workspace setup
    work_dir = base_build_dir / f"work_{sol_file.stem}"
    work_dir.mkdir(exist_ok=True, parents=True)
    
    # 3. Create proxy header
    proxy_header = work_dir / "solution_proxy.h"
    with open(proxy_header, "w") as f:
        f.write(f'#include "{sol_file.resolve()}"')
    
    # 4. Configure (Only if cache missing)
    if not (work_dir / "CMakeCache.txt").exists():
        subprocess.run(["cmake", "-S", str(source_dir), "-B", str(work_dir)], 
                       capture_output=True, check=True)

    # 5. Build
    binary_name = f"run_test_unittest_{prob_id}"
    error_type = "None"
    
    try:
        build_result = subprocess.run(
            ["cmake", "--build", str(work_dir), "--target", binary_name], 
            capture_output=True, text=True, timeout=TIMEOUT_COMPILE
        )
    except subprocess.TimeoutExpired:
        return {"prob_id": prob_id, "attempt_num": attempt_num, "result": "failed", 
                "error_type": "Timeout (Compilation)", "raw_stderr": "Build timed out"}

    # 6. Execute
    if build_result.returncode == 0:
        try:
            binary_path = work_dir / binary_name
            proc = subprocess.run([str(binary_path)], capture_output=True, text=True, timeout=TIMEOUT_EXECUTE)
            result = "pass" if proc.returncode == 0 else "failed"
            error_type = "None" if proc.returncode == 0 else "Assertion Failure"
            stderr_output = proc.stdout
        except subprocess.TimeoutExpired:
            result, error_type, stderr_output = "failed", "Timeout (Runtime)", "Execution timed out"
    else:
        result, stderr_output = "failed", build_result.stderr
        #error_type = "Syntax/Compilation Error"
        error_type = "Exception"
        
    return {
        "prob_id": prob_id,
        "attempt_num": attempt_num,
        "result": result,
        "error_type": error_type,
        "raw_stderr": stderr_output
    }
def run_parallel_tests(unittest_files_dir: str):
    source_dir = Path(unittest_files_dir)
    base_build_dir = source_dir / "builds_parallel"
    base_build_dir.mkdir(exist_ok=True)
    
    solution_files = list(source_dir.glob("solution_*.cpp"))
    
    # Parallel processing
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [executor.submit(run_single_task, f, source_dir, base_build_dir) for f in solution_files]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
            results_num = len(results)
            if results_num % 30 or results_num == 1:
                print(f"Added {len(results)}/{len(solution_files)} results")
            
    # Cleanup: remove the workspace folder after task is done
    # shutil.rmtree(base_build_dir) # Optional: uncomment if you want to clear after run
    return results

import json
from collections import defaultdict

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
                "difficulty": meta.get("difficulty"),
                "attempts": [],
                "passed_attempts": 0,
                "failed_attempts": 0
            }
            
        # Update attempt stats
        problem_map[prob_id]["attempts"].append({
            "attempt_number": res["attempt_num"],
            "result": res["result"],
            "error_type": res["error_type"],
            "raw_stderr": res["raw_stderr"]
        })
        
        if res["result"] == "pass":
            problem_map[prob_id]["passed_attempts"] += 1
        else:
            problem_map[prob_id]["failed_attempts"] += 1
            
        # Finalize total
        problem_map[prob_id]["total_attempts"] = len(problem_map[prob_id]["attempts"])

    # Save to JSON
    with open(output_file_path, "w") as f:
        json.dump(list(problem_map.values()), f, indent=4)
        
    print(f"Successfully saved {len(problem_map)} problem results to {output_file_path}")

    return len(problem_map)

def classify_python_error(stderr: str) -> str:
    """
    Analyzes the stderr text to determine the category of the failure.
    """
    # These are code crashes, not logical assertions
    crash_patterns = [
        "NameError", 
        "SyntaxError", 
        "ImportError", 
        "ModuleNotFoundError", 
        "AttributeError", 
        "TypeError"
    ]
    
    if any(pattern in stderr for pattern in crash_patterns):
        #return "Syntax/Import/Runtime Error"
        return "Exception"
    
    # If it's not a crash but it failed, it's an assertion error
    if "AssertionError" in stderr or "FAILED" in stderr:
        return "Assertion Failure"
        
    return "Unknown Error"


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
    # 1. Structure to hold results grouped by ID
    problem_map = {}
    tests_added = 0
    
    # 2. Get all solution files (e.g., solution_1_1.py, solution_1_2.py)
    # Sort them to ensure attempts are processed in order
    solution_files = sorted(Path(unittest_files_dir).glob("solution_*.py"))

    for sol_file in solution_files:
        match = re.search(r"solution_(\d+)_(\d+)", sol_file.name)
        if not match: continue
        
        prob_id, attempt_num = match.group(1), match.group(2)
        
        # 3. Initialize entry if ID not seen yet
        if prob_id not in problem_map:
            meta = get_metadata(prob_id)
            problem_map[prob_id] = {
                "id": prob_id,
                "difficulty": meta.get("difficulty"),
                "examples_count": len(meta.get("examples", [])),
                "constraints_count": len(meta.get("constraints", [])),
                "tags": meta.get("tags", []),
                "attempts": []
            }
        
        # 4. Prepare execution environment
        # Point to the existing unittest file for this specific ID
        test_file = Path(unittest_files_dir) / f"test_unittest_{prob_id}.py"
        
        # Pass the specific solution file path to the test via environment variable
        env = os.environ.copy()
        env["TEST_SOLUTION_FILE"] = str(sol_file.absolute())
        
        # 5. Run test
        cmd = ["python3", "-m", "unittest", str(test_file)]
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
        
        attempt_result: str = "pass" if proc.returncode == 0 else "failed"
        # 6. Store attempt result
        problem_map[prob_id]["attempts"].append({
            "attempt_number": int(attempt_num),
            "result": attempt_result,
            "error_type": classify_python_error(proc.stderr) if proc.returncode != 0 else "None",
            "raw_stderr": proc.stderr if proc.returncode != 0 else ""
        })

        total_attempts = len(problem_map[prob_id]["attempts"])

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
        metadata_source = py_record or cpp_record

        merged_entry = {
            "id": problem_id,
            "difficulty": metadata_source.get("difficulty"),
            "examples_count": metadata_source.get("examples_count"),
            "constraints_count": metadata_source.get("constraints_count"),
            "tags": metadata_source.get("tags", []),

            "python": {
                "attempts": [],
                "total_attempts": 0,
                "passed_attempts": 0,
                "failed_attempts": 0
            },

            "cpp": {
                "attempts": [],
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
    """

    Returns:
        int: total records/rows stored
    """

    attempt_rows = []

    for problem in merged_results:

        for language in ["python", "cpp"]:

            lang_data = problem[language]

            for attempt in lang_data["attempts"]:

                attempt_rows.append({
                    "id": problem["id"],
                    "language": language,
                    "difficulty": problem["difficulty"],
                    "examples_count": problem["examples_count"],
                    "constraints_count": problem["constraints_count"],
                    "tags": problem["tags"],

                    "attempt_number": attempt["attempt_number"],
                    "result": attempt["result"],
                    "error_type": attempt["error_type"]
                })
    attempt_df: pd.Dataframe = pd.DataFrame(attempt_rows)
    attempt_df = attempt_df.explode("tags")
    attempt_df.attrs['name'] = 'Leetcode Attempts Results'

    return attempt_df

def generate_problem_dataframe(merged_results):
    problem_rows = []

    for problem in merged_results:

        for language in ["python", "cpp"]:

            lang_data = problem[language]

            attempts = lang_data["attempts"]

            eventually_passed = (
                lang_data["passed_attempts"] > 0
            )

            first_try_success = False

            if attempts:
                first_try_success = (
                    attempts[0]["result"] == "pass"
                )

            problem_rows.append({
                "id": problem["id"],
                "language": language,
                "difficulty": problem["difficulty"],
                "examples_count": problem["examples_count"],
                "constraints_count": problem["constraints_count"],
                "tags": problem["tags"],

                "eventually_passed": eventually_passed,
                "first_try_success": first_try_success,

                "total_attempts": lang_data["total_attempts"],
                "passed_attempts": lang_data["passed_attempts"],
                "failed_attempts": lang_data["failed_attempts"]
            })
    problems_df = pd.DataFrame(problem_rows)
    problems_df = problems_df.explode("tags")
    problems_df.attrs['name'] = 'Leetcode Problems Results'

    return problems_df

def generate_summary_report(result_file_path_cpp: str, result_file_path_py: str):
    """
    Generates a summary report for both C++ and Python unit tests.

    This function should be implemented to compile the evaluation results from both
    C++ and Python tests into a comprehensive summary report.
    """
    pass

def save_current_figure(filename: str) -> None:
    """
    Saves the current matplotlib figure and closes it.
    """

    GRAPH_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    plt.tight_layout()
    plt.savefig(GRAPH_OUTPUT_DIR / filename)
    plt.close()

def generate_graph_report(
    attempt_df: pd.DataFrame,
    problems_df: pd.DataFrame
) -> None:
    """
    Generates graphical analysis reports and saves them to disk.
    """

    GRAPH_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------
    # Python vs C++ Success Rate
    # --------------------------------------------------

    language_success = (
        problems_df
        .groupby("language")["eventually_passed"]
        .mean()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    language_success.plot(kind="bar")

    plt.ylabel("Success Rate")
    plt.xlabel("Language")
    plt.title("Python vs C++ Success Rate")

    save_current_figure("language_success_rate.png")

    # --------------------------------------------------
    # First Attempt Success Rate
    # --------------------------------------------------

    first_try_success = (
        problems_df
        .groupby("language")["first_try_success"]
        .mean()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    first_try_success.plot(kind="bar")

    plt.ylabel("First Attempt Success Rate")
    plt.xlabel("Language")
    plt.title("First Attempt Success Rate")

    save_current_figure("first_attempt_success_rate.png")

    # --------------------------------------------------
    # Difficulty vs Failure Type
    # --------------------------------------------------

    difficulty_failures = (
        attempt_df[attempt_df["result"] == "failed"]
        .groupby(["difficulty", "error_type"])
        .size()
        .unstack(fill_value=0)
    )

    plt.figure(figsize=(10, 6))

    difficulty_failures.plot(kind="bar", stacked=True)

    plt.ylabel("Failure Count")
    plt.xlabel("Difficulty")
    plt.title("Difficulty vs Failure Type")

    save_current_figure("difficulty_vs_failure_type.png")

    # --------------------------------------------------
    # Tag vs Success Rate
    # --------------------------------------------------

    tag_success = (
        problems_df
        .groupby("tags")["eventually_passed"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(12, 6))

    tag_success.plot(kind="bar")

    plt.ylabel("Success Rate")
    plt.xlabel("Tag")
    plt.title("Tag vs Success Rate")

    save_current_figure("tag_success_rate.png")

    print(f"Saved graphs to: {GRAPH_OUTPUT_DIR}")

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
    print(f"\n\n{dashes}")


def main():
    """
    Main function to run all unit tests for generated code.
    """

    parser = argparse.ArgumentParser(description="Cherry pick specific functionality")
    # 4. Define an optional boolean flag to not run cpp and python unittests (True if present, False if absent)
    parser.add_argument("-a", "--analysis_only", action="store_true", help="Skip creation of unittest results to start analysis")
    args = parser.parse_args()
 
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

    """
    print("Generating summary report..")
    generate_summary_report(CPP_UNITTEST_RESULTS_FILE, PY_UNITTEST_RESULTS_FILE)
    """

    generate_graph_report(attempts_df, problems_df)
    print("Summary report generated.")

if __name__ == "__main__":
    main()