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
        - Tag vs success rate
        - Difficulty vs failure type
        - Python vs C++ comparison
        - First-attempt success rate
        -Failure progression analysis
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

PY_UNITTESTS_DIR = "python/"
CPP_UNITTESTS_DIR = "cpp/"

PY_UNITTEST_RESULTS_FILE = "python_test_results.json"
CPP_UNITTEST_RESULTS_FILE = "cpp_test_results.json"

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

def get_error_for_file(build_log: str, source_filename: str) -> str:
    """
    Searches the full build log for the specific file and extracts relevant errors.
    """
    # Isolate the filename
    fname = Path(source_filename).name
    
    # Simple regex to find lines associated with the file
    # It searches for the filename, then grabs the text until the next error or block
    pattern = re.compile(rf"({re.escape(fname)}.*?)(\n\s*\n|make\[)", re.DOTALL)
    match = pattern.search(build_log)
    
    if match:
        return match.group(1).strip()
    return "Compilation failed. Check build logs for details."

def run_and_store_cpp_tests(unittest_files_dir: str, output_file_path: str):
    source_dir = Path(unittest_files_dir)
    build_dir = source_dir / "build"
    proxy_header = source_dir / "solution_proxy.h"
    tests_added = 0
    
    # 1. Ensure build directory exists
    if not build_dir.exists():
        build_dir.mkdir(parents=True)
        subprocess.run(["cmake", "-S", str(source_dir), "-B", str(build_dir)], check=True)

    problem_map = {}
    solution_files = sorted(list(source_dir.glob("solution_*.cpp")))

    for sol_file in solution_files:
        match = re.search(r"solution_(\d+)_(\d+)", sol_file.name)
        if not match: continue
        
        prob_id, attempt_num = match.group(1), match.group(2)
        
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

        # 1. Swap the Proxy Header
        with open(proxy_header, "w") as f:
            f.write(f'#include "{sol_file.name}"')
            f.flush()            # Flush Python's internal buffer
            os.fsync(f.fileno()) # Force the OS to write to disk
            
        # 2. Safety Check: Verify the write
        with open(proxy_header, "r") as f:
            content = f.read()
            if sol_file.name not in content:
                raise IOError("Failed to update proxy header correctly!")

        # 3. Aggressive Clean: Remove only the directory associated with the build
        # This forces CMake to re-evaluate dependencies without nuking the whole build dir
        # (This path depends on your CMake structure, adjust if needed)
        cmake_files_dir = build_dir / "CMakeFiles"
        if cmake_files_dir.exists():
            # Deleting the specific target's directory or the whole folder
            # If performance is an issue, just delete the specific target's .o file
            # For total reliability, delete the directory:
            shutil.rmtree(cmake_files_dir)

        # 4. Build the test binary
        binary_name = f"run_test_unittest_{prob_id}"
        build_result = subprocess.run(
            ["cmake", "--build", str(build_dir), "--target", binary_name], 
            capture_output=True, text=True
        )

        attempt_result: str = None
        # 5. Execute and Record
        if build_result.returncode == 0:
            binary_path = build_dir / binary_name
            proc = subprocess.run([str(binary_path)], capture_output=True, text=True)

            attempt_result = "pass" if proc.returncode == 0 else "failed"
            
            problem_map[prob_id]["attempts"].append({
                "attempt_number": int(attempt_num),
                "result": attempt_result,
                "error_type": "None" if proc.returncode == 0 else "Assertion Failure",
                "raw_stderr": proc.stdout
            })
        else:
            attempt_result = "failed"
            # Handle Compilation/Syntax errors
            problem_map[prob_id]["attempts"].append({
                "attempt_number": int(attempt_num),
                "result": attempt_result,
                "error_type": "Syntax/Compilation Error",
                "raw_stderr": build_result.stderr
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

    with open(output_file_path, "w") as f:
        json.dump(list(problem_map.values()), f, indent=4)

    return tests_added


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
        return "Syntax/Import/Runtime Error"
    
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


def evaluate_cpp_test_results(result_file_path: str):
    """
    Evaluates the results of the C++ unit tests.

    This function should be implemented to analyze the stored C++ test results
    and generate a summary or report.
    """
    pass

def evaluate_python_test_results(result_file_path: str):
    """
    Evaluates the results of the Python unit tests.
    This function should be implemented to analyze the stored Python test results
    and generate a summary or report.
    """
    pass

def generate_summary_report(result_file_path_cpp: str, result_file_path_py: str):
    """
    Generates a summary report for both C++ and Python unit tests.

    This function should be implemented to compile the evaluation results from both
    C++ and Python tests into a comprehensive summary report.
    """
    pass

def generate_graph_report(result_file_path_cpp: str, result_file_path_py: str):
    """
    Generates a graphical report for both C++ and Python unit tests using numpy graphs.

    This function should be implemented to create visual representations (e.g., charts, graphs)
    of the test results for better insights.
    """
    pass

def main():
    """
    Main function to run all unit tests for generated code.
    """
    
    print("Running Python unit tests...")
    tests_added_py = run_and_store_python_tests(PY_UNITTESTS_DIR, PY_UNITTEST_RESULTS_FILE)
    print(f"Added {tests_added_py} Python tests to results.")

    print("Running C++ unit tests...")
    tests_added_cpp = run_and_store_cpp_tests(CPP_UNITTESTS_DIR, CPP_UNITTEST_RESULTS_FILE)
    print(f"Added {tests_added_cpp} C++ tests to results.")

    """
    print("Evaluating Python test results...")
    evaluate_python_test_results(PY_UNITTEST_RESULTS_FILE)
    print("Evaluating C++ test results...")
    evaluate_cpp_test_results(CPP_UNITTEST_RESULTS_FILE)

    print("Generating summary report..")
    generate_summary_report(CPP_UNITTEST_RESULTS_FILE, PY_UNITTEST_RESULTS_FILE)

    generate_graph_report(CPP_UNITTEST_RESULTS_FILE, PY_UNITTEST_RESULTS_FILE)
    print("Summary report generated.")
    """

if __name__ == "__main__":
    main()