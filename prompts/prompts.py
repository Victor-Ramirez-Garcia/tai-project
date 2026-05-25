import json

PROBLEMS_FILE_LOCATION = "../problem_extraction/leetcode_library.json"
PROMPT_FILE_LOCATION = "prompts.txt"

def generate_prompts(json_filename, output_filename):
    with open (json_filename, "r") as f:
        problems = json.load(f)
    
    with open(output_filename, "w") as f:
        for p in problems:
            # 3. Format the text for the LLM
            prompt = (
                f"--- Problem ID: {p['id']} ---\n"
                f"Question: {p['question']}\n\n"
            )
            f.write(prompt)

def main():
    generate_prompts(PROBLEMS_FILE_LOCATION, PROMPT_FILE_LOCATION)

if __name__ == "__main__":    
    main()