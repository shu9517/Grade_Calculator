# Grade Calculator

A simple, user-friendly desktop application built with Python and `customtkinter` designed to help university students track their academic progress, calculate their Cumulative Grade Point Average (CGPA), and predict needed scores for individual courses.

## Features

*   **📊 CGPA Calculator:** 
    *   Easily input your courses and letter grades (A+, A, A-, B+, etc.).
    *   Supports calculating your GPA based on either a 4.0 scale or a 12.0 scale (or both simultaneously).
*   **📝 Course Score Calculator:** 
    *   Keep track of individual assignments, quizzes, midterms, and finals.
    *   Enter the weight and current score for each component.
    *   Automatically calculates your current percentage and tells you the exact score you need on pending items to pass or reach your target score.
*   **⚙️ Settings:**
    *   **Bilingual Support:** Switch instantly between English and Traditional Chinese (繁體中文).
    *   **Customizable GPA Display:** Choose your preferred GPA format.
*   **💾 Save & Load Data:**
    *   Save your current grades, courses, and settings to a JSON file.
    *   Load them up the next time you open the app so you never lose your progress.

## Prerequisites

Before running the application, make sure you have Python installed along with the required `customtkinter` library:

```bash
pip install customtkinter
```

## How to Run

**On Windows:**
Simply double-click the `run.bat` file included in the project folder.

**Using Terminal/Command Prompt:**
Navigate to the directory containing the project files and run:
```bash
python grade_calc.py
```

## Usage Tips
*   Leave the score blank for "Pending" assignments in the Course Calculator to see how much you need to score on them.
*   Your data isn't saved automatically, so make sure to use the **Save Data** button on the main menu to export your progress before closing.
