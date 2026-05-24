# TAI PROJECT

**NOTE**: We currently only have the gemini model available.

## Setup

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

**NOTE**: Playwright needs Python to be 3.8+

## high-level/
### File Structure
```
constants.py # contains constants
app.py # generates and saves code
testing.py # tests code
gemini/ # shown after running app.py
    medium/
        (leetcode problem number)/
            py/
                trial_#.py
```

### constants.py: The constants
- `BASE_DIR`: the base directory path to `high-level/`
- `LEETCODE_PROBLEMS`: where you can add leetcode problems. For an entry, it contains
    - `problem`: description of the problem
    - `level`: difficulty of the problem
    - `name`: name of the problem
    - `id`: id of the problem
    - `hallucination`: the metric for errors (that is, the error categories). Each category contains a `passed` field and `failed` field. The `passed` field is the number of assertions passed from all trials. The `failed` field is the number of assertions failed from all trials. This is calculated in `analysis.py`
        - `syntactic`: syntax violations, unable to parse, compile, interpret
        - `runtime_execution`: exceptions, crashes, during execution
        - `functional_correctness`: can execute code but does not satisfy requirements of the program
- `CONSTRAINTS`: where you can add additional context to a leetcode problem. For an entry, it contains
    - `prompt`: Additional context that is added to a leetcode problem
    - `ext`: file extension used for constructing the file path
- `SITES`: where you can add a new model (a free site is required). For a pair, the key is the model's name and the value is a dictionary containing a key-value pair for the url site (accessed with key `site`).
- `LOCATOR`: List of HTML elements that are used to find a textbox of a site to type in a prompt.
- `SELECTOR`: List of HTML elements that are used to select the generated code for parsing and saving to a new file

### app.py: Running the program
DEFINITIONS
- contraint: Additional context that is attached to the leetcode problem to specify anything. The constraint also contains the file extension (e.g. py, cpp) which is used to specify the type of file.

PROCESS
1. initializes the trial counter for a leetcode problem to the next available file. The purpose is to auto-save the generated code.
2. For each leetcode problem, the program follows the format below:
    - Opens a headless Chrome browser
    - Creates a browser context that doesn't share cookies/cache
    - Go to Step 3
    - After Step 3 is completed:
        - Closes browser
        - Waits x seconds until moving to the next leetcode problem
3. For each constraint:
    - Constructs the prompt to be sent to the model by concatenating the leetcode problem with the constraint
    - Go to Step 4
4. For each model:
    - Creates a new page
    - Go to model's site
    - Locate textbox
    - Clicks on textbox
    - Removes any text within textbox by auto-press Ctrl+A, Backspace
    - Types prompt
    - Press Enter
    - Gets and saves the generated code to the next available file
    - Closes page and clear cookies

### testing.py: Testing the generated code
DEFINITIONS
- contraint: Additional context that is attached to the leetcode problem to specify anything. The constraint also contains the file extension (e.g. py, cpp) which is used to specify the type of file.
- trial: generated program for a particular leetcode problem.

PROCESS
1. For each leetcode problem, the program follows the format below:
    - Go to Step 2
2. For each contraint:
    - Go to Step 3
3. For each model:
    - Go to Step 4
    - After Step 4 is completed:
        - Display the results
4. For each trial:
    - Run tests. Each test increments either the `passed` field or the `failed` failed for a particular error category. The tests that are currently shown include
        - CLASS NAME NOT FOUND (runtime execution)
        - METHOD NOT FOUND (runtime execution)
        - TEST OUTPUT DOES NOT MATCH EXPECTED OUTPUT (functional correctness)

## low-level/
Currently Empty.