import json

PROBLEMS_FILE_LOCATION = "../problem_extraction/leetcode_library.json"
PROMPT_FILE_LOCATION = "prompts.json"

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
            output_list.append({
                "id": entry.get("id"),
                "language": lang,
                "question": entry.get("question"),
                "starter_code": starter_code.get(lang, "")
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