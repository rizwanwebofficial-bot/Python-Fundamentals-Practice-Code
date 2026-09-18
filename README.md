# Python Fundamentals – Practice Code

The code I wrote while learning Python in the **AI Ka Chilla** course by [**Ammar Bin Tufail**](https://github.com/AammarTufail). It covers the core building blocks of the language, one topic per file, plus a notebook of small practice exercises.

> [!NOTE]
> **This is a beginner-level learning repository.** The files are short demonstrations and practice programs, not a project.

---

## Contents

| File | Topic | What it shows |
|---|---|---|
| `01_operators.py` | Operators | A reference of every operator group (arithmetic, comparison, assignment, logical, bitwise, membership, identity, special, walrus `:=`) with examples, plus a string concatenation demo |
| `02_variables.py` | Variables and assignment | Simple, multiple, chained and augmented assignment; tuple and `*` unpacking; assigning to dictionary keys and object attributes; loop and comprehension variables; the `_` throwaway variable |
| `03_program1.py` | First small program | Reads two names and ages with `input()` and prints who is older |
| `04_datastructure.py` | Data structures | Lists (`append`, `insert`, indexing), tuples (immutability), sets (duplicates, why `True` disappears next to `1`) and dictionaries |
| `05_control_flow_statement.py` | Control flow | `for` loop with slicing, `if / elif / else`, and a `while` loop using `continue` |
| `06_nested_loops.py` | Nested loops | A loop inside a loop to combine every item of two lists |
| `07_functions.py` | Functions | A simple function, a function with `return`, recursion (factorial) and a lambda |
| `08_modules.py` | Modules | *Placeholder.* Only a `pip install` line for pandas, numpy, matplotlib, seaborn, scipy and statsmodels |

### Practice notebook (`python_practice.ipynb`)

| Section | Exercise |
|---|---|
| Variables and data types | Store student details, check types with `type()`, calculate a percentage |
| Type casting | Convert between `int`, `float`, `str` and `bool` (including which strings count as `True`), then compute total and average marks |
| Arithmetic operators | Shopping bill: total price, discount amount, price after discount, price per item |
| Comparison operators | Pass/fail and attendance checks combined with `and` |
| Conditional statements | Withdrawal check: invalid amount, insufficient balance, or remaining balance |
| Loops | Take `n` from the user, then print 1 to `n` (`for`), sum 1 to `n` (`while`), and label each number even or odd |

---

## Concepts Practiced

Variables and data types, type casting, operators, `if / elif / else`, `for` and `while` loops, nested loops, lists, tuples, sets, dictionaries, functions (return values, recursion, lambda), f-strings, and reading user input.

---

## How to Run

Requires Python 3.8 or newer.

```bash
python 01_operators.py
python 03_program1.py        # asks for input in the terminal
jupyter notebook python_practice.ipynb
```

`04_datastructure.py` intentionally includes lines that assign to a tuple to demonstrate the `TypeError`, so the script stops at that point. Comment those two lines out to run the set and dictionary sections.

---

## Credits

Course: **AI Ka Chilla** by [Ammar Bin Tufail](https://github.com/AammarTufail)
