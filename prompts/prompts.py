import json

PROBLEMS_FILE_LOCATION = "../problem_extraction/leetcode_library.json"
PROMPT_FILE_LOCATION = "prompts.json"

# Instructions for the Gemini LLM to follow when generating the solution 
# for each of the LeetCode problem prompts. 
LLM_INSTRUCTION_SOLUTION = """
You are an expert competitive programmer and software engineer. Your task is to provide the 
optimal implementation for the provided LeetCode problem in the specified programming language.

STRICT GUIDELINES:
1. IMPLEMENTATION: Complete the provided 'starter_code' exactly. Do not rename classes or function 
   signatures, as the solution must be compatible with standard LeetCode test runners.
2. EFFICIENCY: Prioritize the most optimal Time and Space complexity. Explain your choice of 
   algorithm (e.g., Two Pointers, Sliding Window, DP) if necessary within comments.
3. CONSTRAINTS & EDGE CASES: Ensure your code handles all provided 'constraints' and edge cases 
   (e.g., empty inputs, negative numbers, or integer overflows).
4. STYLE: Write idiomatic code. For C++, use modern standards (C++17/20) and appropriate STL 
   containers. For Python, use type hints as provided in the starter code.
5. FORMATTING: Return ONLY the code inside the class structure. Do not include markdown 
   explanations before or after the code block. The output must be ready to be parsed as a 
   raw string and placed directly into an IDE.
6. COMMENTS: Include concise comments explaining the core logic, especially for non-trivial parts.
7. DEPENDENCIES & COMPILABILITY (MANDATORY):
   - PYTHON: You MUST include all necessary imports at the top (e.g., 'from typing import List, Optional, Deque'). 
     If using any type hints (List, Optional, etc.), the import is non-negotiable.
   - C++: You MUST include all necessary standard library headers (e.g., #include <vector>, #include <string>, #include <algorithm>, #include <queue>).
   - STRUCTURES: If the problem involves custom structures (ListNode, TreeNode) and they are not explicitly 
     defined in the starter code, YOU MUST define the struct at the top of your solution file so the code is self-contained.
"""

LLM_INSTRUCTION_UNITTEST = """
You are a Quality Assurance engineer expert in unit testing. Your task is to write a comprehensive 
unit test file for the provided LeetCode problem.

STRICT GUIDELINES:
1. FRAMEWORK: 
   - For C++, use the GoogleTest (gTest) framework. 
   - For Python, use the standard 'unittest' module. Create a class that inherits from 'unittest.TestCase'.
2. COVERAGE: You must write test cases that cover:
   - All 'examples' provided in the problem description.
   - Key edge cases identified from the 'constraints' (e.g., minimum/maximum input sizes, empty inputs).
3. INTEGRATION: Assume the user's solution is in a header file or the same file. Use proper assertions 
   (e.g., EXPECT_EQ for gTest, self.assertEqual for unittest).
4. FORMATTING: Return ONLY the code for the test file. Do not include markdown conversational filler. 
   The output must be a raw code block ready to be saved as a test file (e.g., 'test_solution.cpp' 
   or 'test_solution.py').
5. CLARITY: Each test method should have a descriptive name reflecting the scenario being tested 
   (e.g., 'test_empty_input', 'test_large_value_constraint').
6. IMPORT REQUIREMENT: The solution will be saved in a file named 'solution_{id}_1.{ext}'. 
   Your test file must import the 'Solution' class from this specific file. 
   - For Python: Use 'from solution_{id}_1 import Solution'.
   - For C++: Use '#include "solution_{id}_1.cpp"'.
7. NO MAIN FUNCTION: Do not include a 'main()' function in your C++ test file. The build system 
   (CMake/gTest) provides the 'main()' function automatically. Adding one will cause build errors.
"""


def process_problems(input_filename, output_filename) -> int:
    # 1. Load the entire input file (must be a valid JSON array)
    with open(input_filename, "r", encoding="utf-8") as f:
        input_data = json.load(f) # This is now a list of objects
    
    # 2. Initialize or load the output file
    output_list = []
    
    # 3. Loop through each object
    for entry in input_data:
        # Here you can filter, transform, or log the data
        print(f"Processing ID: {entry.get('id')}")
        
        starter_code = entry.get("starter_code", {})

        # Loop through each language to create an entry
        for lang in starter_code.keys():
            lang_slug = lang.lower()
            if lang_slug == "python":
                lang_slug = "py" # adjust for leetcode's language slug
            
            if lang_slug not in ["py", "cpp"]:
                print(f"Skipping unsupported language '{lang}' for ID: {entry.get('id')}")
                continue

            # Use a single f-string to handle the entire prompt construction
            prompt_solution_text = (
                f"{LLM_INSTRUCTION_SOLUTION}\n\n"
                f"PROBLEM STATEMENT:\n{entry.get('question')}\n\n"
                f"EXAMPLES:\n{chr(10).join(entry.get('examples', []))}\n\n"
                f"CONSTRAINTS:\n{chr(10).join(entry.get('constraints', []))}\n\n"
                f"STARTER CODE ({lang_slug.upper()}):\n{starter_code.get(lang, '')}"
            )

            # Use a single f-string to handle the entire prompt construction
            prompt_unittest_text = (
                f"{LLM_INSTRUCTION_UNITTEST}\n\n"
                f"PROBLEM STATEMENT:\n{entry.get('question')}\n\n"
                f"EXAMPLES:\n{chr(10).join(entry.get('examples', []))}\n\n"
                f"CONSTRAINTS:\n{chr(10).join(entry.get('constraints', []))}\n\n"
                f"STARTER CODE ({lang_slug.upper()}):\n{starter_code.get(lang, '')}"
            )

            output_list.append({
                "leetcode-problem-id": entry.get("id"),
                "language": lang_slug,
                "prompt_solution": prompt_solution_text,
                "prompt_unittest": prompt_unittest_text,
                "generated_program_paths": [],
	            "file_counter": 0,
            })
        
    # 4. Save the final list as a valid JSON array
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(output_list, f, indent=4)
        
    return len(output_list)

def main():
    # Run the process
    count = process_problems(PROBLEMS_FILE_LOCATION, PROMPT_FILE_LOCATION)
    print(f"Finished. {count} objects written to {PROMPT_FILE_LOCATION}")

if __name__ == "__main__":    
    main()