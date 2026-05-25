import requests
import json

def get_leetcode_problem(url):
    # Extract the title slug from the URL
    slug = url.rstrip('/').split('/')[-1]
    
    # LeetCode's GraphQL endpoint
    api_url = "https://leetcode.com/graphql"
    
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                difficulty
                content
                topicTags {
                    name
                }
            }
        }
        """,
        "variables": {"titleSlug": slug}
    }
    
    response = requests.post(api_url, json=query)
    data = response.json()
    
    if "data" in data and data["data"]["question"]:
        return data["data"]["question"]
    else:
        print(f"Failed to retrieve: {slug}")
        return None

# --- Usage Example ---
problem_urls = [
    "https://leetcode.com/problems/two-sum/",
    "https://leetcode.com/problems/add-two-numbers/"
]

problem_list = []

for url in problem_urls:
    problem_data = get_leetcode_problem(url)
    if problem_data:
        problem_list.append(problem_data)

# Save to a file
with open("leetcode_problems.json", "w") as f:
    json.dump(problem_list, f, indent=4)

print("Successfully saved problems to leetcode_problems.json")