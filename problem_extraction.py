import requests
import json

def get_leetcode_problem_extended(url):
    slug = url.rstrip('/').split('/')[-1]
    api_url = "https://leetcode.com/graphql"
    
    # Added codeSnippets to the query
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
                    lang
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
    
    return data  # Debug: Print the raw API response

# --- Example Usage ---
url = "https://leetcode.com/problems/two-sum/"

problem_data = get_leetcode_problem_extended(url)
print(json.dumps(problem_data, indent=4))