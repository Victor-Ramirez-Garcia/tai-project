import requests
import json
from bs4 import BeautifulSoup

def get_leetcode_problem_structured(url, target_lang='python3'):
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
        soup = BeautifulSoup(q['content'], 'html.parser')
        
        # 1. Extract Question Body (text before first example)
        question_text = ""
        for element in soup.children:
            if element.name == 'p' and "Example" in element.get_text():
                break
            question_text += element.get_text() + "\n"
            
        # 2. Extract Examples
        examples = []
        for strong in soup.find_all('strong', class_='example'):
            pre = strong.find_next('pre')
            if pre:
                examples.append(pre.get_text().strip())
        
        # Replace your current constraints extraction with this:
        constraints = []
        ul = soup.find('ul')
        if ul:
            for li in ul.find_all('li'):
                # This preserves the power-of-ten notation by converting <sup> tags
                for sup in li.find_all('sup'):
                    sup.insert_before('^')
                constraints.append(li.get_text().strip())

        return {
            "id": q["questionId"],
            "title": q["title"],
            "question": question_text.strip(),
            "examples": examples,
            "constraints": constraints,
            "starter_code": next((s['code'] for s in q['codeSnippets'] if s['langSlug'] == target_lang), "")
        }
    return None

# Usage
url = "https://leetcode.com/problems/two-sum/"
print(json.dumps(get_leetcode_problem_structured(url), indent=4))