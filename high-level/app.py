import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).resolve().parent

LEETCODE_PROBLEMS = [
    {
        "problem": """Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).""",
        "level": "medium",
        "id": "7"
    },
    {
        "problem": """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.""",
        "level": "medium",
        "id": "15"
    }
]

CONSTRAINTS = [
    {
        "prompt": "Only provide the code in Python.",
        "ext": "py"
    }
]

REPHRASE_CONSTRAINT = "Rephrase this problem that contains real life context"

LOCATOR = 'div[contenteditable="true"][role="textbox"]'

SITES = {
    "gemini": {"site": "https://gemini.google.com/app"}
}

SELECTORS = [
    'code[data-test-id="code-content"]',
]

WAIT_FOR_NEW_BROWSER = 20

def prework():
    """
    Sets the trial counter's to the next available file.
    """
    print("initializing trial counter's")
    for leet in LEETCODE_PROBLEMS: # for each leetcode problem
        for constraint in CONSTRAINTS: # for each contraint
            ext = constraint["ext"] # get prog lang ext (e.g. py, cpp)
            for model, _ in SITES.items(): # for each model (e.g. gemini, openai)
                leet[model] = 1 # init trial counter
                # get path to leetcode problem directory
                LEET_DIR = f"{leet['level']}_{leet['id']}"
                CODE_ROOT = BASE_DIR / model / LEET_DIR
                CODE_ROOT.mkdir(parents=True, exist_ok=True) # create directory if dne

                # set trial counter to next available file
                while ((CODE_ROOT / f"trial_{leet[model]}.{ext}").exists()):
                    leet[model] += 1
    return None



def get_generated_code(page, timeout=60000):
    """
    Parses the pages response and returns the generated code.
    """
    # get element locator to find any of the list of selectors,
    # and wait until at least one element appears
    combined_selector = ", ".join(SELECTORS)
    locator = page.locator(combined_selector)
    locator.first.wait_for(state="visible", timeout=timeout)

    # return the code block. otherwise, raise TimeoutError
    count = locator.count()
    if count == 0:
        raise TimeoutError("No code block found.")
    return locator.first.inner_text().strip()

def save_code(code, leet, model, ext):
    """
    Saves the code to the leetcode problem's directory and increments trial counter.
    """
    # get path to leetcode problem directory
    LEET_DIR = f"{leet['level']}_{leet['id']}"
    FILE = f"trial_{leet[model]}.{ext}"
    CODE_ROOT = BASE_DIR / model / LEET_DIR / FILE
    CODE_ROOT.parent.mkdir(parents=True, exist_ok=True)

    # save code to file
    with open(CODE_ROOT, 'w') as f:
        f.write(code)

    leet[model] += 1 # increment trial counter for the particular model and leetcode problem
    return None

def main():
    with sync_playwright() as p:
        prework()

        for leet in LEETCODE_PROBLEMS: # for each leetcode problem
            browser = p.chromium.launch(headless=True) # create new headless browser (browser that does not pop up)
            context = browser.new_context() # create new browser context that doesnt share cookies/cache with other browser context
            for constraint in CONSTRAINTS: # for each constraint
                PROMPT = leet["problem"] + ' ' + constraint["prompt"] # construct prompt
                for model, site in SITES.items(): # for each model
                    # create new page, go to site, locate textbox, click on textbox,
                    # remove any text (if it contains any), type and enter the prompt
                    # to generate the code
                    page = context.new_page()
                    page.goto(site["site"])
                    textbox = page.locator(LOCATOR)
                    textbox.wait_for()
                    textbox.click()
                    page.keyboard.press("Control+A")
                    page.keyboard.press("Backspace")
                    page.keyboard.type(PROMPT)
                    textbox.press("Enter")

                    # get and save generated code to leetcode problem path
                    code = get_generated_code(page)
                    save_code(code, leet, model, constraint["ext"])

                    # close page and clear cookies from context
                    page.close()
                    context.clear_cookies()
            browser.close()
            print(f"completion generations for problem #{leet["id"]} (wait for {WAIT_FOR_NEW_BROWSER} seconds)")
            time.sleep(WAIT_FOR_NEW_BROWSER)

main()