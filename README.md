# student-data-base-
data base for students of 2025
# Student Database Management System

A command-line Python program that stores the academic records of 60 students (4 subjects each). From a simple menu you can search a student by registration number, see the overall topper, or print every student's report card. Grades, remarks and attendance are colour-coded in the terminal.

It runs completely from the terminal. No GUI, database server or internet connection is needed.

## Project files

| File | Purpose |
|---|---|
| `main.py` | The program (menu, search, topper, show-all) |
| `student_database.json` | Student data (60 students, 4 subjects each) |
| `requirements.txt` | Dependency list (empty - only the standard library is used) |
 | These instructions |

## Setup and run (step by step)

### 1. Prerequisites

- Python 3.6 or newer
- A terminal (Command Prompt, PowerShell, Windows Terminal, macOS Terminal, Linux shell, or the VS Code terminal)
- Git (only if you want to clone the repository; you can also download it as a ZIP)

Check that Python is installed:

```
python --version
```

On macOS/Linux, use `python3 --version`. If the command is not found, install Python from https://www.python.org/downloads/ and tick "Add Python to PATH" during installation.

### 2. Get the project

Option A - clone with Git:

```
git clone https://github.com/<github-username>/<repo-name>.git
cd <repo-name>
```

Option B - download: on the GitHub page click **Code -> Download ZIP**, extract it, and open a terminal inside the extracted folder.

Make sure `main.py` and `student_database.json` are in the **same folder**.

### 3. Environment setup (optional but recommended)

Create and activate a virtual environment:

```
python -m venv venv
```

Windows:
```
venv\Scripts\activate
```

macOS / Linux:
```
source venv/bin/activate
```

You can skip steps 3 and 4 on Windows/macOS; the project works with the system Python too.

### 4. Install dependencies

The project uses only the Python standard library, so nothing extra is required. To keep the setup standard, you can still run this (with the virtual environment from step 3 active; on some Linux systems pip refuses to run outside one):

```
pip install -r requirements.txt
```

This finishes without installing anything.

### 5. Configuration

No configuration is needed. The program automatically loads `student_database.json` from the same folder as `main.py`.

To change the data, edit `student_database.json`. The file must stay valid JSON, and every student needs the same fields as the existing records.

### 6. Run the program

```
python main.py
```

(`python3 main.py` on macOS/Linux.)

## Using the program

```
1. Search student      -> type a registration number, e.g. 26BCE10001
2. Show overall topper -> student with the highest overall aggregate
3. Show ALL students   -> prints all 60 report cards
4. Exit
```

Expected result for option 1 with `26BCE10001`: a report card for ABHIJITH PRABHAKARAN showing all four subjects, overall aggregate 98.2 %, semester GPA 10.0 / 10 and result status PROMOTED.
Option 2 prints: `Overall Topper: ABHIJITH PRABHAKARAN (26BCE10001) - 98.2%`.

## Marking scheme (each subject, out of 100)

| Component | Marks | Weightage |
|---|---|---|
| CAT 1 | out of 50 | 15 |
| CAT 2 | out of 50 | 15 |
| FAT | out of 100 | 30 |
| Internals (group activities) | out of 10 | 10 |
| Assignment | out of 10 | 10 |
| Discussion | out of 10 | 10 |
| Quizzes | out of 10 | 10 |

## Grades, remarks and colours

| Marks | Grade | Remark | Colour |
|---|---|---|---|
| 90 - 100 | S | Excellent | Green |
| 80 - 89 | A | Outstanding | Blue |
| 70 - 79 | B | Good | Blue |
| 60 - 69 | C | Keep it up | Blue |
| 50 - 59 | D | Needs improvement | Light red |
| 40 - 49 | E | Just passed | Light red |
| below 40 | F | Not eligible for next sem | Red |

Attendance: 90% and above = Excellent (green), 75% to below 90% = Good (blue), below 75% = Critical (red).

A student with grade F in any subject gets the result status `NOT ELIGIBLE FOR NEXT SEM`.

## How the code is organised

- `gi(g)` - returns the colour for a grade
- `ai(a)` - returns the colour for an attendance value
- `show(db, r)` - prints the report card of one registration number
- `main()` - loads the JSON file and runs the menu loop

## Troubleshooting

| Problem | Fix |
|---|---|
| `FileNotFoundError` for the JSON file | Keep `student_database.json` in the same folder as `main.py` and don't rename it |
| `python` is not recognised | Use `python3` or `py main.py`, or reinstall Python with "Add to PATH" ticked |
| Text like `[92;1m` appears instead of colours | Use Windows Terminal, PowerShell or the VS Code terminal instead of old CMD |
| "Student not found" | Registration numbers look like `26BCE10001` (case does not matter) |
