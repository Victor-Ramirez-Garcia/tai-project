import time, json
from playwright.sync_api import sync_playwright
from playwright._impl._errors import TargetClosedError
from constants import (
    BASE_DIR, SITES, LOCATOR, SELECTORS
)

TRIALS = 1 # number of trials to run
WAIT_FOR_NEW_BROWSER = 10 # time (in seconds) to wait for a new browser

PROMPT_PATH = BASE_DIR / "prompts" / "prompts.json"

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
        CODE_ROOT = BASE_DIR / "generated_code" / prompt["leetcode-problem-id"] / prompt["language"]
        FILENAME = f"program_{prompt['file_counter']}.{prompt['language']}"
        
        # set file counter to next available file
        while ((CODE_ROOT / FILENAME).exists()):
            prompt['file_counter'] += 1
            FILENAME = f"program_{prompt['file_counter']}.{prompt['language']}"
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
    page.keyboard.insert_text(prompt)
    textbox.press("Enter")

    return page


def get_generated_code(page, timeout=60000):
    combined_selector = ", ".join(SELECTORS)
    locator_main = page.locator(combined_selector)
    locator_two = page.locator('p[data-path-to-node="0"]')

    try:
        locator_main.first.wait_for(state="attached", timeout=timeout)
    except TargetClosedError:
        return ""
    except Exception:
        return ""

    start_time = page.evaluate("Date.now()")

    prev_text = ""
    stable_count = 0

    while True:
        try:
            main_text = locator_main.first.text_content() or ""

            two_text = ""
            if locator_two.count() > 0:
                two_text = locator_two.first.text_content() or ""

            # if error/status node appears → abort extraction
            if two_text.strip():
                return ""

            # detect stability of main text
            if main_text == prev_text:
                stable_count += 1
            else:
                stable_count = 0
                prev_text = main_text

            # only return once stable for a few cycles AND non-empty
            if stable_count >= 3 and main_text.strip():
                return main_text.strip()

            if page.evaluate("Date.now()") - start_time > timeout:
                raise TimeoutError("Timed out waiting for stable code output")

            page.wait_for_timeout(300)

        except TargetClosedError:
            # Page/browser/context closed while polling
            return ""


def save_code(code, prompt) -> None:
    """
    Saves the code to the leetcode problem's directory and sets trial
    counter to next available file.
    """
    # get path to leetcode problem directory
    FILENAME = f"program_{prompt['file_counter']}.{prompt['language']}"
    CODE_ROOT = BASE_DIR / "generated_code" / prompt["leetcode-problem-id"] / prompt["language"]
    CODE_ROOT.mkdir(parents=True, exist_ok=True)

    # save code to file
    with open(CODE_ROOT / FILENAME, 'w') as f:
        f.write(code)
    
    # append file path to prompt
    prompt["generated_program_paths"].append(CODE_ROOT / FILENAME)

    # set trial counter to next available file
    while ((CODE_ROOT / FILENAME).exists()):
        prompt["file_counter"] += 1
        FILENAME = f"program_{prompt['file_counter']}.{prompt['language']}"


def main():
    prompts = set_file_counters() # loads prompts and initializes file counter's
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # create new headless browser (browser that does not pop up)
        context = browser.new_context() # create new browser context that doesnt share cookies/cache with other browser context
        for prompt in prompts:
            code = ""

            while code == "":
                page = generate_code(SITES["gemini"], prompt["prompt"], context) # goes to site, enters prompt, and generates the code

                # get and save generated code to leetcode problem path
                code = get_generated_code(page)
                if code != "":
                    save_code(code, prompt)
                else:
                    # close page and clear cookies from context
                    page.close()
                    context.clear_cookies()

                    print(f"failed {prompt["language"]} generation for #{prompt["leetcode-problem-id"]} (wait for {WAIT_FOR_NEW_BROWSER} seconds)")
                    time.sleep(WAIT_FOR_NEW_BROWSER)
            # close page and clear cookies from context
            page.close()
            context.clear_cookies()
            print(f"success {prompt["language"]} generation for #{prompt["leetcode-problem-id"]} (wait for {WAIT_FOR_NEW_BROWSER} seconds)")
            time.sleep(WAIT_FOR_NEW_BROWSER)


        # close browser and wait x seconds
        browser.close()
    save_prompts(prompts)


if __name__ == "__main__":
    trial = 0
    while (trial < TRIALS):
        main()
        trial += 1