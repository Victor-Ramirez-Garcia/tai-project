import requests
import re
import os
import datetime
import json
from bs4 import BeautifulSoup

"""
with open("leetcode_library.json", "r") as f:
    my_problems = json.load(f)

# You now have a list of dictionaries ready to iterate through!
for problem in my_problems:
    print(f"Working on: {problem['title']}")
"""

OUTPUT_LIBRARY_FILE: str = "leetcode_library.json" 

def save_to_library(problem_data, filename=OUTPUT_LIBRARY_FILE) -> bool:
    """
    Appends a new problem to a JSON file. 
    If the file exists, it loads it, appends the new entry, and saves it.
    """
    library = []
    
    # Load existing library if it exists
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                library = json.load(f)
            except json.JSONDecodeError:
                library = []
    
    # Check if problem is already in the library to avoid duplicates
    if not any(p['id'] == problem_data['id'] for p in library):
        library.append(problem_data)
        with open(filename, "w") as f:
            json.dump(library, f, indent=4)
        return True
    else:
        print(f"Problem '{problem_data['title']}' is already in the library.")
        return False

def get_leetcode_problem_structured(url):
    slug = url.rstrip('/').split('/')[-1]
    api_url = "https://leetcode.com/graphql"
    
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                difficulty
                topicTags { name } 
                content
                codeSnippets { langSlug code }
            }
        }
        """,
        "variables": {"titleSlug": slug}
    }
    
    response = requests.post(api_url, json=query)
    data = response.json()
    
    if "data" in data and data["data"].get("question"):
        q = data["data"]["question"]
        # Use a string replace to clean up non-breaking spaces immediately
        content_html = q['content'].replace('\u00a0', ' ')
        soup = BeautifulSoup(content_html, 'html.parser')
        
        # 1. Extract Question Body
        question_text = ""
        for element in soup.children:
            if element.name == 'p' and "Example" in element.get_text():
                break
            question_text += element.get_text() + "\n"
            
        # 2. Extract Examples
        examples = [pre.get_text().strip() for pre in soup.find_all('pre')]
        
        # 3. Extract Constraints (with improved superscript handling)
        constraints = []
        ul = soup.find('ul')
        if ul:
            for li in ul.find_all('li'):
                # Convert <sup> tags to '^' for math readability
                for sup in li.find_all('sup'):
                    sup.insert_before('^')
                constraints.append(li.get_text().strip())
            
        # 4. Extract Snippets
        snippets = {s['langSlug']: s['code'] for s in q['codeSnippets']}
        
        tags = [tag['name'] for tag in q.get('topicTags', [])]

        return {
            "id": q["questionId"],
            "title": q["title"],
            "difficulty": q["difficulty"],
            "tags": tags, 
            "question": clean_text(question_text),
            "examples": [clean_text(ex) for ex in examples],
            "constraints": [clean_text(c) for c in constraints],
            "starter_code": {
                "python": snippets.get('python3', 'Not available'),
                "cpp": snippets.get('cpp', 'Not available')
            }
    }
    print(f"Couldn't retrieve the problem under this url: `{url}`")
    return None

def clean_text(text):
    """Normalize whitespace and remove non-breaking spaces."""
    # Replace non-breaking space with normal space
    text = text.replace('\u00a0', ' ')
    # Replace multiple newlines or spaces with single ones
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

# --- Usage Example ---

with open("urls.txt", "r") as f:
    problem_urls = [line.strip() for line in f if line.strip()]

if os.path.exists(OUTPUT_LIBRARY_FILE):
    print(f"Flushing old {OUTPUT_LIBRARY_FILE}")
    os.remove(OUTPUT_LIBRARY_FILE)

total_problems = len(problem_urls)
saved_problems = 0
for url in problem_urls:
    data = get_leetcode_problem_structured(url)
    if data:
        did_add = save_to_library(data)
        if did_add:
            saved_problems += 1

print(f"Saved {saved_problems}/{total_problems} leetcode problems.")