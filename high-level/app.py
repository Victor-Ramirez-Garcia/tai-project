import time, json
from pathlib import Path
from playwright.sync_api import sync_playwright
from constants import (
    BASE_DIR, SITES, LOCATOR, SELECTORS
)

TRIALS = 1 # number of trials to run
WAIT_FOR_NEW_BROWSER = 20 # time (in seconds) to wait for a new browser

PROMPT_PATH = BASE_DIR / "prompt.json"

def load_prompts() -> dict:
    """
    Loads the constructed prompts from file.
    """
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_prompts(prompts) -> None:
    """
    Saves the prompts to file.
    """
    with open(PROMPT_PATH, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2)


def set_file_counters() -> dict:
    """
    Sets the file counter's to the next available file.
    """
    prompts = load_prompts() # loads prompts

    print("initializing trial counter's")
    for prompt in prompts: # for each leetcode problem
        prompt['file_counter'] = 1
        # get path to leetcode problem directory
        CODE_ROOT = BASE_DIR / "generated_code" / prompt["id"] / prompt["file_extension"]
        FILENAME = f"program_{prompt['file_counter']}.{prompt['file_extension']}"
        
        # set file counter to next available file
        while ((CODE_ROOT / FILENAME).exists()):
            prompt['file_counter'] += 1
            FILENAME = f"program_{prompt['file_counter']}.{prompt['file_extension']}"
    return prompts


def generate_code(site, prompt, context):
    """
    Opens site, enters prompt, and generates the code.
    """
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
    page.keyboard.type(prompt)
    textbox.press("Enter")

    return page


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


def save_code(code, prompt) -> None:
    """
    Saves the code to the leetcode problem's directory and sets trial
    counter to next available file.
    """
    # get path to leetcode problem directory
    FILENAME = f"program_{prompt['file_counter']}.{prompt['file_extension']}"
    CODE_ROOT = BASE_DIR / "generated_code" / prompt["id"] / prompt["file_extension"]
    CODE_ROOT.mkdir(parents=True, exist_ok=True)

    # save code to file
    with open(CODE_ROOT / FILENAME, 'w') as f:
        f.write(code)
    
    # append file path to prompt
    prompt["generated_program_paths"].append(CODE_ROOT / FILENAME)

    # set trial counter to next available file
    while ((CODE_ROOT / FILENAME).exists()):
        prompt["file_counter"] += 1
        FILENAME = f"program_{prompt['file_counter']}.{prompt['file_extension']}"


def main():
    prompts = set_file_counters() # loads prompts and initializes file counter's
    with sync_playwright() as p:
        for prompt in prompts:
            browser = p.chromium.launch(headless=True) # create new headless browser (browser that does not pop up)
            context = browser.new_context() # create new browser context that doesnt share cookies/cache with other browser context
            page = generate_code(SITES["gemini"], prompt, context) # goes to site, enters prompt, and generates the code

            # get and save generated code to leetcode problem path
            code = get_generated_code(page)
            save_code(code, prompt)

            # close page and clear cookies from context
            page.close()
            context.clear_cookies()

            # close browser and wait x seconds
            browser.close()
            print(f"completion generations for problem #{prompt["id"]} (wait for {WAIT_FOR_NEW_BROWSER} seconds)")
            time.sleep(WAIT_FOR_NEW_BROWSER)
    save_prompts(prompts)


if __name__ == "__main__":
    trial = 0
    while (trial < TRIALS):
        main()
        trial += 1