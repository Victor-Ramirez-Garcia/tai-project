import requests
import json

def get_leetcode_problem_cleaned(url, target_lang='python3'):
    slug = url.rstrip('/').split('/')[-1]
    api_url = "https://leetcode.com/graphql"
    
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                difficulty
                content
                topicTags { name }
                codeSnippets {
                    langSlug
                    code
                }
            }
        }
        """,
        "variables": {"titleSlug": slug}
    }
    
    response = requests.post(api_url, json=query)
    data = response.json()
    
    # Check if data exists and is valid
    if "data" in data and data["data"].get("question"):
        q = data["data"]["question"]
        
        # Extract and format the specific code snippet
        snippet = next(
            (s['code'] for s in q['codeSnippets'] if s['langSlug'] == target_lang), 
            "Snippet not found"
        )
        
        # Create a cleaned dictionary
        cleaned_data = {
            "id": q["questionId"],
            "title": q["title"],
            "difficulty": q["difficulty"],
            "tags": [tag["name"] for tag in q["topicTags"]],
            "content": q["content"],
            "starter_code": snippet
        }
        return cleaned_data
    return None

# --- Usage ---
url = "https://leetcode.com/problems/two-sum/"
problem = get_leetcode_problem_cleaned(url)

if problem:
    # This prints the dictionary in a "pretty" readable format
    print(json.dumps(problem, indent=4))