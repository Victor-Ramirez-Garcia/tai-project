import requests
import re
import json
from bs4 import BeautifulSoup

def get_leetcode_problem_structured(url):
    slug = url.rstrip('/').split('/')[-1]
    api_url = "https://leetcode.com/graphql"
    
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
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
        
        return {
            "id": q["questionId"],
            "title": q["title"],
            "question": clean_text(question_text),
            "examples": [clean_text(ex) for ex in examples],
            "constraints": [clean_text(c) for c in constraints],
            "starter_code": {
                "python": snippets.get('python3', 'Not available'),
                "cpp": snippets.get('cpp', 'Not available')
            }
    }
    return None

def clean_text(text):
    """Normalize whitespace and remove non-breaking spaces."""
    # Replace non-breaking space with normal space
    text = text.replace('\u00a0', ' ')
    # Replace multiple newlines or spaces with single ones
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

# --- Testing ---
url = "https://leetcode.com/problems/two-sum/"
print(json.dumps(get_leetcode_problem_structured(url), indent=4))