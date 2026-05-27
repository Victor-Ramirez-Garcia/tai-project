"""
unittest_run_all.py

- Runs unit tests for all generated code for both C++ and Python, separately.
    - The results should be redirected to a file, python and cpp separately, for later evaluation.
        - Since python doesn't compile the code before running, we can directly run the tests and capture the results.
        - For C++, we need to compile the code first and then run the tests, capturing the results.
- Stores the results of each unittest in a structured JSON format for later evaluation for both C++ and Python, separately.
    - Each stored record should include the following information:
    - Leetcode Id
    - Result (pass/failed)
    - Error type if an (Syntax, Runtime, Logical/Assertion)
    - Difficulty
    - Number of examples provided
    - Number of constraints provided
    
- Evaluates the results of the tests and generates a summary or report for both C++ and Python, separately.
    - The evaluation report should include metrics such as 
        - The number of tests passed, failed
        - Which failures were caused by Syntax, Runtime, or Logical/Assertion errors
        - What was the leetcode `difficulty` for each of the passed or failed test
        - What were the leetcode `tags` for each of the the passed or failed test
        - How many leetcode `examples` were provided for each of the passed or failed test
        - How many leetcode `constraints` were provided for each of the passed or failed test
"""

import os
import json
import subprocess
import re
from pathlib import Path

PY_UNITTESTS_DIR = "py/"
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

def run_and_store_cpp_tests(unittest_files_dir: str, output_file_path: str) -> int:
    """
    Discovers and runs C++ unit tests for all generated code.

    This function should be implemented to find and execute C++ unit tests,
    and store the results in a structured format (e.g., JSON, XML).

    Args:
        unittest_files_dir (str): The directory where C++ unit test files are located.
        output_file_path (str): The file path where the test results should be stored.
    """
    results = []
    tests_added = 0
    build_dir = Path(unittest_files_dir) / "build"
    source_dir = Path(unittest_files_dir)

    # 1. Ensure project is configured
    if not (build_dir / "CMakeCache.txt").exists():
        build_dir.rmdir(parents=True, exist_ok=True)
        build_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["cmake", "-S", str(source_dir), "-B", str(build_dir)], capture_output=True)

    # 2. Build the project AND capture the full log
    build_proc = subprocess.run(
        ["cmake", "--build", str(build_dir), "--", "-k"], 
        capture_output=True, 
        text=True # Important to get a string, not bytes
    )
    full_build_log = build_proc.stderr 

    # 3. Iterate through SOURCE test files
    for source_file in source_dir.glob("test_unittest_*.cpp"):
        match = re.search(r"unittest_(\d+)", source_file.name)
        if not match: continue
        
        problem_id = match.group(1)
        meta = get_metadata(problem_id)
        
        binary_name = f"run_test_unittest_{problem_id}" 
        binary_path = build_dir / binary_name
        
        if binary_path.exists():
            # SUCCESS: Run it
            proc = subprocess.run([str(binary_path)], capture_output=True, text=True)
            result = "pass" if proc.returncode == 0 else "failed"
            raw_stderr = proc.stderr if proc.returncode != 0 else ""
            error_type = "None" if proc.returncode == 0 else "Assertion"
        else:
            # FAILURE: Binary missing -> Search the log for the cause
            result = "failed"
            error_type = "Syntax/Compilation"
            raw_stderr = get_error_for_file(full_build_log, source_file.name)

        results.append({
            "id": problem_id,
            "result": result,
            "error_type": error_type,
            "difficulty": meta.get("difficulty"),
            "examples_count": len(meta.get("examples", [])),
            "constraints_count": len(meta.get("constraints", [])),
            "raw_stderr": raw_stderr
        })
        tests_added += 1
        
    with open(output_file_path, "w") as f:
        json.dump(results, f, indent=4)
        
    return tests_added
   

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
    results = []    
    tests_added = 0
    # Search for test files
    files: list[Path] = list(Path(unittest_files_dir).glob("test_unittest_*.py"))

    for file in files:
        match = re.search(r"unittest_(\d+)", file.name)
        if not match:
            continue
        problem_id = match.group(1)
        
        meta = get_metadata(problem_id)
        
        # FIX: Run via the unittest module. 
        # This forces the test suite to execute and provides reliable exit codes.
        # 0: Success
        # 1: Test failed (AssertionError)
        # 2: Error (Runtime/Import/Syntax error)
        cmd = ["python3", "-m", "unittest", file.name]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=unittest_files_dir)

        if proc.returncode == 0:
            result = "pass"
            error_type = "None"
        else:
            result = "failed"
            error_type = classify_python_error(proc.stderr)

        results.append({
            "id": problem_id,
            "result": result,
            "error_type": error_type,
            "difficulty": meta.get("difficulty"),
            "examples_count": len(meta.get("examples", [])),
            "constraints_count": len(meta.get("constraints", [])),
            # Capture stderr for both assertions and crashes
            "raw_stderr": proc.stderr if proc.returncode != 0 else ""
        })
        tests_added += 1
        
    with open(output_file_path, "w") as f:
        json.dump(results, f, indent=4)
    
    return tests_added


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

    """
    print("Running C++ unit tests...")
    tests_added_cpp = run_and_store_cpp_tests(CPP_UNITTESTS_DIR, CPP_UNITTEST_RESULTS_FILE)
    print(f"Added {tests_added_cpp} C++ tests to results.")

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