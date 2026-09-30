.# Student Database Management System (CLI)

A lightweight, terminal-based academic evaluation and student records viewer written in Python. This tool parses JSON-formatted student academic records and formats detailed grade sheets, attendance tracking, and performance analytics into an ANSI-colorized tabular interface.

---

## Problem Statement & Objective

Academic evaluation systems often require inspecting complex multi-component metrics per subject (Continuous Assessment Tests [CAT1, CAT2], Final Assessment Test [FAT], internal marks, assignments, discussions, and quizzes) alongside attendance metrics. 

The objective of this project is to provide a fast, dependency-free CLI tool for educators, administrators, and students to:
1. Search and view individual student transcripts with formatted tabular breakdown.
2. Monitor attendance risk levels (Critical, Good, Excellent) mapped with visual indicators.
3. Compute and highlight overall semester performance, GPA, aggregate percentages, and academic promotion status.
4. Identify top-performing students across the cohort (`Overall Topper`).

---

## 🚀 Key Features

- **Zero External Dependencies**: Operates entirely with Python standard libraries (`json`, `os`).
- **ANSI Terminal Color Coding**:
  - **Grades**: Green for top tier (`S`), Blue for passing standard (`A`, `B`, `C`), Soft Red for marginal grades (`D`, `E`), and Bold Red for failure/risk.
  - **Attendance Health**:
    - $\ge 90\%$: Green (`Excellent`)
    - $75\% - 89.9\%$: Blue (`Good`)
    - $< 75\%$: Red (`Critical`)
- **Granular Subject Breakdown**:
  - Continuous Assessment: CAT-1, CAT-2, Internal marks
  - Continuous Engagements: Assignments, Discussion forum scores, Quizzes
  - Summative: Final Assessment Test (FAT) & Computed Final Scores
- **Cohort Analytics**: Fast calculation of the highest aggregate scorer in the dataset.

---

##  Data Structure Specification

The program expects a `student_database.json` file in the same directory as the script. The JSON schema must follow this structure:

```json
{
  "REG2026001": {
    "name": "Jane Doe",
    "overall_aggregate": 88.5,
    "semester_gpa": 8.9,
    "average_attendance": 92.4,
    "result_status": "PROMOTED",
    "subjects": {
      "Data Structures": {
        "attendance": 94.0,
        "cat1": 45,
        "cat2": 48,
        "fat": 88,
        "internal": 28,
        "assignment": 10,
        "discussion": 5,
        "quizzes": 10,
        "final_score": 91.5,
        "grade": "S",
        "remark": "Outstanding"
      }
    }
  }
}
```

---

##  Usage Instructions

### Prerequisites
- Python 3.7+
- A terminal supporting ANSI escape sequences (Linux/macOS terminals, Windows Terminal, VS Code Integrated Terminal)

### Installation & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-database-management-system.git
   cd student-database-management-system
   ```

2. Place your `student_database.json` in the root folder alongside the script.

3. Run the script:
   ```bash
   python main.py
   ```

### Menu Options
```text
1. Search student        -> Query record by registration number (case-insensitive)
2. Show overall topper   -> Find student with maximum overall aggregate
3. Show ALL students     -> Print grade sheets for all entries in the database
4. Exit                  -> Quit application
```

---

##  Sample Output Preview

```text
=================================================================================================================================================
STUDENT DATABASE MANAGEMENT SYSTEM
=================================================================================================================================================
Registration Number: REG2026001
Name: Jane Doe
-------------------------------------------------------------------------------------------------------------------------------------------------
Subject                  Attendance        CAT1 CAT2  FAT  Int Assign Discuss  Quiz   Marks  Grade   Remark
Data Structures           94.0% Excellent    45   48   88   28      10       5    10   91.50      S   Outstanding
-------------------------------------------------------------------------------------------------------------------------------------------------
Overall Aggregate: 88.5 %  | Semester GPA: 8.9 / 10  | Average Attendance: 92.4 %
Result Status: PROMOTED
=================================================================================================================================================
```

---

##  Roadmap & Future Enhancements

- [ ] Add CRUD operations (add, edit, delete students directly via CLI).
- [ ] Implement input error handling for corrupt or missing JSON files.
- [ ] Export transcripts to CSV or PDF formats.
- [ ] Add sorting filters (by GPA, by attendance risk, by subject).
