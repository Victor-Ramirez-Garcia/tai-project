import time, json, os, random
from pathlib import Path
from playwright.sync_api import sync_playwright
from playwright._impl._errors import TargetClosedError
from concurrent.futures import ThreadPoolExecutor, as_completed
from constants import (
    BASE_DIR, SITES, LOCATOR, SELECTORS
)

TRIALS = 1 # number of trials to run
PROMPT_PATH = BASE_DIR / "prompts" / "prompts.json" # path to prompts.json
MAX_WORKERS = 1 # number of concurrent threads

def wait_for_new_page(a=10, b=25):
    delay = random.uniform(a,b)
    if random.random() < 0.1:
        delay += random.uniform(30,130)
    return delay

def load_prompts() -> list:
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
        json.dump(prompts, f, indent=4)


def set_file_counters() -> list:
    """
    Sets the file counter's to the next available file.
    """
    prompts = load_prompts() # loads prompts

    print("initializing trial counter's")
    for prompt in prompts: # for each leetcode problem
        prompt['file_counter'] = 1
        # get path to leetcode problem directory
        CODE_ROOT = BASE_DIR / "generated_code" / prompt["language"]
        FILENAME = f"solution_{prompt['leetcode-problem-id']}_{prompt['file_counter']}.{prompt['extension']}"
        
        # set file counter to next available file
        while ((CODE_ROOT / FILENAME).exists()):
            prompt['file_counter'] += 1
            FILENAME = f"solution_{prompt['leetcode-problem-id']}_{prompt['file_counter']}.{prompt['extension']}"

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
    page.wait_for_timeout(200)
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


def save_code(code, prompt, is_unittest: bool) -> None:
    """
    Saves the code to the leetcode problem's directory and sets trial
    counter to next available file.
    """
    CODE_ROOT = BASE_DIR / "generated_code" / prompt["language"]
    CODE_ROOT.mkdir(parents=True, exist_ok=True)

    if is_unittest == False:
        # get path to leetcode problem directory
        FILENAME = f"solution_{prompt['leetcode-problem-id']}_{prompt['file_counter']}.{prompt['extension']}"
    else:
        FILENAME = f"test_unittest_{prompt['leetcode-problem-id']}.{prompt['extension']}"

    # save code to file
    with open(CODE_ROOT / FILENAME, 'w') as f:
        f.write(code)
    
    if is_unittest == False:
        # append file path to prompt
        prompt["generated_program_paths"].append(Path(os.path.relpath(CODE_ROOT / FILENAME, start=Path(__file__).parent)).as_posix())

        # set trial counter to next available file
        while ((CODE_ROOT / FILENAME).exists()):
            prompt["file_counter"] += 1
            FILENAME = f"solution_{prompt['leetcode-problem-id']}_{prompt['file_counter']}.{prompt['extension']}"


def generate_program(prompt, context, is_unittest: bool) -> None:
    """
    Generates a program.
    """
    code = ""

    while True:
        if is_unittest == False:
            page = generate_code(SITES["gemini"], prompt["prompt_solution"], context) # goes to site, enters prompt, and generates the code
        else:
            page = generate_code(SITES["gemini"], prompt["prompt_unittest"], context) # goes to site, enters prompt, and generates the code

        # get and save generated code to leetcode problem path
        code = get_generated_code(page)
        if code != "":
            save_code(code, prompt, is_unittest)
            # close page and clear cookies from context
            page.close()
            context.clear_cookies()
            break

        # close page and clear cookies from context
        page.close()
        context.clear_cookies()

        WAIT_FOR_NEW_PAGE = wait_for_new_page()
        if is_unittest == False:
            print(f"failed {prompt["language"]} generation for solution #{prompt["leetcode-problem-id"]} (wait for {WAIT_FOR_NEW_PAGE} seconds)")
        else:
            print(f"failed {prompt["language"]} generation for unittest #{prompt["leetcode-problem-id"]} (wait for {WAIT_FOR_NEW_PAGE} seconds)")
        wait_for_new_page()
    WAIT_FOR_NEW_PAGE = wait_for_new_page()
    if is_unittest == False:
        print(f"success {prompt["language"]} generation for solution #{prompt["leetcode-problem-id"]} (wait for {WAIT_FOR_NEW_PAGE} seconds)")
    else:
        print(f"success {prompt["language"]} generation for unittest #{prompt["leetcode-problem-id"]} (wait for {WAIT_FOR_NEW_PAGE} seconds)")

def process_prompt(prompt):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # create new headless browser (browser that does not pop up)
        context = browser.new_context() # create new browser context that doesnt share cookies/cache with other browser context
        try:
            generate_program(prompt, context, False) # generate program

            CODE_ROOT = BASE_DIR / "generated_code" / prompt["language"]
            UNITTEST_FILENAME = f"test_unittest_{prompt['leetcode-problem-id']}.{prompt['extension']}"
            # skip unittest if it exists (we only need one)
            if not (CODE_ROOT / UNITTEST_FILENAME).exists():
                generate_program(prompt, context, True) # generate unittest
        finally:
            context.close() # close context
            browser.close() # close browser

def main():
    """
    Generates programs and unittests for each leet problem in prompts.json.
    """
    prompts = set_file_counters() # loads prompts and initializes file counter's
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(process_prompt, prompt)
            for prompt in prompts
        ]
        for future in as_completed(futures):
            future.result()
    save_prompts(prompts) # save updated entries in prompts


if __name__ == "__main__":
    trial = 0
    while (trial < TRIALS):
        main()
        trial += 1