"""
pipeline.py

Automatically executes the python, specifically:

1. Extract problems
    - Runs `problem_extraction/problem_extraction.py` to extract the problems
    - Store results in `problem_extraction/test_leetcode_library.json `
2. Generate LLM prompts to generate solutions and unittests
    - Runs `prompts/prompts.py` to generate the prompts for solution and unittests
    - Store results in `prompts/prompts.json`
3. Generate solutions and unittests using LLM
    - Runs `solution_generation/solution_generation.py` to generate the solutions and unittests
    - Store results in `solution_generation/solutions.json`
    - Note: This step may require multiple runs to generate all solutions and unittests due to rate limits and potential errors

?
4. Run unittests to validate the generated solutions
    - Runs `unittest_execution/unittest_execution.py` to execute the unittests against the generated solutions
    - Store results in `unittest_execution/unittest_results.json`
?

"""