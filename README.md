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

### File Structure
```
generated_code/ # shown after running high-level/app.py
    (leetcode problem number)/
        py/
        cpp/
```

## high-level/
### File Structure
```
constants.py # contains constants
app.py # generates and saves code
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
- `TRIALS`: Number of trials to run
- `WAIT_FOR_NEW_BROWSER`: time (in seconds) to wait for a new browser to open
    - **NOTE**: a browser opens for each prompt
- `PROMPT_PATH`: path to prompts.json

PROCESS
1. initializes the file counter for a leetcode problem to the next available file. The purpose is to auto-save the generated code.
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


To run python unittests, navigate to generated_code/py/ and run `python3 -m unittest discover -v`
## low-level/
Currently Empty.

To use cmake, install VScode extention: `https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools`

To test in the generated_code/cpp/
```bash
# 1. Create a build directory to keep things clean
mkdir build
cd build

# 2. Configure the project (this finds GTest and generates build files)
cmake ..

# 3. Compile all test executables
cmake --build .

# 4. Execute all tests and report results
ctest --output-on-failure

# Or  ./run_tests_401
```