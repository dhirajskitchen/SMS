# School Management System (SMS)

A Python command-line school management system for managing students, teachers, classes, attendance, marks, timetables, applications, and parent interactions.

## Overview

This project uses CSV files in the `data/` folder as its storage backend. It supports different user roles with separate workflows:

- Applicants
- Students
- Parents
- Teachers
- Principals

## Prerequisites

- Python 3.8 or later
- `pandas`

## Installation

1. Open a terminal in the project root directory.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Initialize Data

If the CSV data files do not exist or you want to refresh the sample dataset, run:

```bash
python data/fill_data.py
```

This creates or overwrites sample files in the `data/` folder.

## Running the Application

Start the CLI application from the project root:

```bash
python main.py
```

Choose a role from the main menu and follow the prompts.

## User Roles

### Applicant

- Submit a new application
- Check application status

### Student

- View student details
- Edit student details
- View marks
- View timetable
- View attendance details

### Parent

- View student details
- Edit student details
- View student marks
- Pay fees

### Teacher

- View class details
- View student details
- Enter marks
- Mark attendance
- Create or edit timetables

### Principal

- View class details
- View student details
- View application submissions

## Project Structure

- `main.py` — program entry point
- `utils.py` — common helper functions and validation logic
- `data/` — data loading, storage, and CSV utilities
- `applicant/` — applicant-related modules
- `student/` — student-related modules
- `parent/` — parent-related modules
- `teacher/` — teacher-related modules
- `principal/` — principal-related modules

## Data Files

The application uses the following CSV files in the `data/` folder:

- `students.csv`
- `teachers.csv`
- `subjects.csv`
- `classes.csv`
- `marks.csv`
- `attendance.csv`
- `timetable.csv`
- `application.csv`

## Notes

- CSV storage means data persists across runs when saved.
- Re-run `python data/fill_data.py` to regenerate sample data.
- For best results, run the app from the project root so file paths resolve correctly.
