import json

PROBLEMS_FILE_LOCATION = "../problem_extraction/leetcode_library.json"
PROMPT_FILE_LOCATION = "prompts.json"

# Instructions for the Gemini LLM to follow when generating the solution 
# for each of the LeetCode problem prompts. 
LLM_INSTRUCTION = """
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
            if lang == "python":
                lang = "py" # adjust for leetcode's language slug
            if lang not in ["py", "cpp"]:
                print(f"Skipping unsupported language '{lang}' for ID: {entry.get('id')}")
                continue
            prompt = {
                "llm_instruction": LLM_INSTRUCTION,
                "question": entry.get("question"),
                "starter_code": starter_code.get(lang, ""),
                "examples": entry.get("examples", []),
                "constraints": entry.get("constraints", []),
            }
            output_list.append({
                "leetcode-problem-id": entry.get("id"),
                "language": lang,
                "prompt": prompt,
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