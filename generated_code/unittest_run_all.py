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

def extract_compiler_error(build_log: str, source_filename: str) -> str:
    """
    Collects every line in the build log that references the specific source file.
    """
    filename = os.path.basename(source_filename)
    lines = build_log.splitlines()
    
    # Filter for lines that mention the file and keep a small window of context (e.g., +2 lines)
    error_lines = []
    for i, line in enumerate(lines):
        if filename in line:
            # Add the error line
            error_lines.append(line)
            # Optionally add the next 2 lines for context (like the caret '^')
            error_lines.extend(lines[i+1:i+3])
            
    return "\n".join(error_lines)

def classify_cpp_error(stderr: str, return_code: int) -> str:
    """
    Analyzes stderr and return code to classify C++ errors.
    """
    # If the binary crashed (segfault, abort, etc.)
    if return_code < 0:
        return "Runtime/Segfault"
    
    # Check for GTest or common assertion patterns
    if "FAILED" in stderr or "Assertion" in stderr or "check failed" in stderr:
        return "Assertion"
        
    return "Runtime/Other"

def classify_python_error(stderr: str) -> str:
    """
    Analyzes stderr to determine if it's a Logic/Assertion failure 
    or a Code/Syntax/Name error.
    """
    if not stderr:
        return "Unknown"
    
    # Check for specific Python crash indicators
    if any(err in stderr for err in ["SyntaxError", "NameError", "ImportError", "AttributeError", "TypeError"]):
        return "Syntax/Name/Import Error"
    
    # If it's a test runner failure, it usually contains 'AssertionError' or 'FAILED'
    if "AssertionError" in stderr or "FAILED" in stderr:
        return "Assertion"
        
    return "Runtime/Other"
    
def run_and_store_cpp_tests(unittest_files_dir: str, output_file_path: str):
    """
    Discovers and runs C++ unit tests for all generated code.

    This function should be implemented to find and execute C++ unit tests,
    and store the results in a structured format (e.g., JSON, XML).

    Args:
        unittest_files_dir (str): The directory where C++ unit test files are located.
        output_file_path (str): The file path where the test results should be stored.
    """
def run_and_store_cpp_tests(unittest_files_dir: str, output_file_path: str) -> int:
    results = []
    tests_added = 0
    build_dir = Path(unittest_files_dir) / "build"
    source_dir = Path(unittest_files_dir)

    # 1. Ensure project is configured
    if not (build_dir / "CMakeCache.txt").exists():
        build_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["cmake", "-S", str(source_dir), "-B", str(build_dir)], capture_output=True)

    # 2. Build the project (keep going even if errors occur)
    # We ignore the return code here because we will check file existence later
    build_proc = subprocess.run(["cmake", "--build", str(build_dir), "--", "-k"], 
                                capture_output=True, text=True)
    build_log = build_proc.stderr # Compiler errors usually go to stderr

    # 3. Iterate through SOURCE test files (This is our source of truth)
    for source_file in source_dir.glob("test_unittest_*.cpp"):
        match = re.search(r"unittest_(\d+)", source_file.name)
        if not match: continue
        
        problem_id = match.group(1)
        meta = get_metadata(problem_id)
        
        # Determine the binary name expected by CMakeLists.txt
        # NOTE: Make sure this pattern matches what you have in your CMakeLists.txt
        binary_name = f"run_test_unittest_{problem_id}" 
        #binary_path = build_dir / binary_name
        binary_path = build_dir / f"run_test_unittest_{problem_id}"
        
        if binary_path.exists():
            # SUCCESS: Binary exists, run it
            proc = subprocess.run([str(binary_path)], capture_output=True, text=True)
            
            if proc.returncode == 0:
                result = "pass"
                error_type = "None"
                raw_stderr = ""
            else:
                result = "failed"
                error_type = classify_cpp_error(proc.stderr, proc.returncode)
                raw_stderr = proc.stderr
        else:
            # FAILURE: Extract the specific error
            result = "failed"
            error_type = "Syntax/Compilation"
            raw_stderr = extract_compiler_error(build_log, str(source_file))

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
        # Extract ID
        match = re.search(r"unittest_(\d+)", file.name)
        if not match:
            continue
        problem_id = match.group(1)
        
        # Get metadata (assuming this function is defined elsewhere in your script)
        meta = get_metadata(problem_id)
        
        # FIX: Run the file directly as a script instead of using 'python3 -m unittest'
        # This treats the file as an executable script rather than a module.
        # We set cwd to unittest_files_dir so the script can resolve its own imports.
        cmd = ["python3", file.name]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=unittest_files_dir)

        print(f"Running {file.name}... Return code: {proc.returncode}")

        # Determine status based on return code
        # 0: Pass, 1: Assertion failure, >1: Syntax/Import/Runtime error
        if proc.returncode == 0:
            result = "pass"
            error_type = "None"
        else:
            result = "failed"
            # Use our new classifier
            error_type = classify_python_error(proc.stderr)
            
        results.append({
            "id": problem_id,
            "result": result,
            "error_type": error_type,
            "difficulty": meta.get("difficulty"),
            "examples_count": len(meta.get("examples", [])),
            "constraints_count": len(meta.get("constraints", [])),
            "raw_stderr": proc.stderr if proc.returncode != 0 else "" # Useful for debugging
        })
        tests_added += 1
        
    with open(output_file_path, "w") as f:
        json.dump(results, f, indent=4)
    
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