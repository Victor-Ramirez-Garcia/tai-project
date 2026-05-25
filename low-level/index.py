from leetscrape import GetQuestion

# The 'titleSlug' is the last part of the URL, e.g., 'two-sum'
problem = GetQuestion(titleSlug="two-sum").scrape()

# 'problem' now contains a structured object with:
# description, constraints, examples, code snippets, and more.
import json
print(json.dumps(problem, indent=4))