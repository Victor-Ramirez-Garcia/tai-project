import importlib.util
from constants import (
    BASE_DIR, LEETCODE_PROBLEMS, CONSTRAINTS, SITES
)

CLASS_NAME = "Solution"


def load_module(file, name):
    spec = importlib.util.spec_from_file_location(name, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_tests(leet, file):
    hallucination = leet.get("hallucination", {})
    if hallucination == {}:
        raise ValueError("run_tests(): hallucination tests is empty")

    name = file.stem
    syntactic = hallucination["syntactic"]
    runtime_execution = hallucination["runtime_execution"]
    functional_correctness = hallucination["functional_correctness"]

    module = load_module(file, name)

    # ASSERT #1: CLASS NAME NOT FOUND
    if not hasattr(module, CLASS_NAME):
        runtime_execution["failed"] += 1
    else:
        runtime_execution["passed"] += 1

    try:
        sol = module.Solution()
    except Exception:
        sol = None
    
    method = getattr(sol, leet["name"], None) # gets class method

    # ASSERT #2: METHOD NOT FOUND
    if not method:
        runtime_execution["failed"] += 1
    else:
        runtime_execution["passed"] += 1

    for (test_input, expected) in functional_correctness["tests"]:
        # ASSERT #3: TEST OUTPUT DOES NOT MATCH EXPECTED OUTPUT
        try:
            test_output = method(test_input)

            if test_output != expected:
                functional_correctness["failed"] += 1
            else:
                functional_correctness["passed"] += 1
        except Exception:
            functional_correctness["failed"] += 1
    
    
def log(leet, model):
    """
    displays the results for the leetcode problem
    """
    print("="*50)
    print(f"****RESULTS FOR PROBLEM #{leet["id"]} ({leet["level"]}, {model})****")
    for category, category_dict in leet.get("hallucination", {}).items():
        passed = category_dict.get("passed", 0)
        failed = category_dict.get("failed", 0)
        print(f"{category}\tpassed:{passed}\tfailed:{failed}")


def main():
    for leet in LEETCODE_PROBLEMS: # for each leetcode problem
        for constraint in CONSTRAINTS: # for each contraint
            ext = constraint["ext"] # get prog lang ext (e.g. py, cpp)
            if ext != "py":
                continue
            for model, _ in SITES.items(): # for each model (e.g. gemini, openai)
                leet[model] = 1 # trial counter
                # get path to leetcode problem directory
                FILENAME = f"trial_{leet[model]}.{ext}"
                CODE_ROOT = BASE_DIR / model / leet['level'] / leet['id'] / ext

                # run tests for each trial's program
                # metric: for a given hallucination category, you get # of tests passed and # of tests failed
                while ((CODE_ROOT / FILENAME).exists()):
                    run_tests(leet, CODE_ROOT / FILENAME)
                    leet[model] += 1
                    FILENAME = f"trial_{leet[model]}.{ext}"

                log(leet, model) # display results

                # later: save results in .csv file for trustworthy AI analysis

if __name__ == "__main__":
    main()