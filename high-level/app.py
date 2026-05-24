import time
from pathlib import Path
from playwright.sync_api import sync_playwright
from constants import (
    BASE_DIR, LEETCODE_PROBLEMS, CONSTRAINTS, SITES, LOCATOR,
    SELECTORS
)

TRIALS = 3 # number of trials to run
WAIT_FOR_NEW_BROWSER = 20 # time (in seconds) to wait for a new browser


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
                CODE_ROOT = BASE_DIR / model / leet['level'] / leet['id'] / constraint["ext"]
                CODE_ROOT.mkdir(parents=True, exist_ok=True) # create directory if dne
                FILENAME = f"trial_{leet[model]}.{ext}"

                # set trial counter to next available file
                while ((CODE_ROOT / FILENAME).exists()):
                    leet[model] += 1
                    FILENAME = f"trial_{leet[model]}.{ext}"
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
    Saves the code to the leetcode problem's directory and sets trial
    counter to next available file.
    """
    # get path to leetcode problem directory
    FILENAME = f"trial_{leet[model]}.{ext}"
    CODE_ROOT = BASE_DIR / model / leet['level'] / leet['id'] / ext
    CODE_ROOT.mkdir(parents=True, exist_ok=True)

    # save code to file
    with open(CODE_ROOT / FILENAME, 'w') as f:
        f.write(code)

    # set trial counter to next available file
    while ((CODE_ROOT / FILENAME).exists()):
        leet[model] += 1
        FILENAME = f"trial_{leet[model]}.{ext}"

    return None


def main():
    with sync_playwright() as p:
        prework() # initialize trial counter's

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


if __name__ == "__main__":
    trial = 0
    while (trial < TRIALS):
        main()
        trial += 1