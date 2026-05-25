from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SITES = {
    "gemini": {"site": "https://gemini.google.com/app"}
}

LOCATOR = 'div[contenteditable="true"][role="textbox"]'

SELECTORS = [
    'code[data-test-id="code-content"]'
]