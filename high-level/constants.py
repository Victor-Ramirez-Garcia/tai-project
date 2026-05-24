from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

LEETCODE_PROBLEMS = [
    {
        "problem": """Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).""",
        "level": "medium",
        "name": "reverse",
        "id": "7",
        "hallucination": {
            "syntactic": {"passed": 0, "failed": 0},
            "runtime_execution": {"passed": 0, "failed": 0},
            "functional_correctness": { "passed": 0, "failed": 0, "tests": [(123, 321), (-123,-321), (120, 21), (0, 0)] }
        }
    },
    {
        "problem": """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.""",
        "level": "medium",
        "name": "threeSum",
        "id": "15",
        "hallucination": {
            "syntactic": {"passed": 0, "failed": 0},
            "runtime_execution": {"passed": 0, "failed": 0},
            "functional_correctness": {"passed": 0, "failed": 0, "tests": [([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]), ([0,1,1], []), ([0,0,0], [[0,0,0]])] }
        }
    }
]

CONSTRAINTS = [
    {
        "prompt": "Only provide the code in Python.",
        "ext": "py"
    }
]

SITES = {
    "gemini": {"site": "https://gemini.google.com/app"}
}

LOCATOR = 'div[contenteditable="true"][role="textbox"]'

SELECTORS = [
    'code[data-test-id="code-content"]'
]