# School Management System (SMS)

A simple Python command-line school management system that manages students, teachers, classes, attendance, marks, timetables, applications, and parent interactions using CSV files as the data store.

## Features

- Student role: view and edit student details, view marks, attendance, and timetable
- Parent role: view student details, view marks, pay fees
- Teacher role: view class details, view student details, enter marks, mark attendance, and manage timetables
- Principal role: view class details, view student details, and review applications
- Applicant role: submit new applications and check application status
- Data stored in CSV files under the `data/` folder

## Prerequisites

- Python 3.8 or later
- `pandas` library

## Setup

1. Open a terminal in the project root directory.
2. Install dependencies:

```bash
python -m pip install pandas
```

3. Generate initial CSV data (optional, if data files are not present or you want fresh sample data):

```bash
python data/fill_data.py
```

## Running the Application

From the project root directory, run:

```bash
python main.py
```

Follow the menu prompts to choose a user type and perform actions.

## User Roles and Use Cases

### Applicant
- Submit application
- Check application status

### Student
- View student details
- Edit student details
- View marks
- View timetable
- View attendance details

### Parent
- View student details
- View student marks
- Pay fees

### Teacher
- View class details
- View student details
- Enter marks
- Mark attendance
- Edit or create timetable

### Principal
- View class details
- View student details
- View applications

## Data Files

The application uses the following CSV files under `data/`:

- `students.csv`
  - `student_id`, `name`, `dob`, `gender`, `class_id`, `attendance_percentage`, `fee_status`
- `teachers.csv`
  - `teacher_id`, `name`, `subject_id`
- `subjects.csv`
  - `subject_id`, `subject_name`
- `classes.csv`
  - `class_id`, `class_grade`, `section`, `subject_ids`, `class_teacher_id`, `strength`
- `marks.csv`
  - `mark_id`, `student_id`, `subject_id`, `teacher_id`, `marks_obtained`, `total_marks`
- `attendance.csv`
  - `attendance_id`, `student_id`, `class_id`, `date`, `status`
- `timetable.csv`
  - `class_id`, `day`, `time_slot`, `subject_id`
- `application.csv`
  - `application_no`, `name`, `dob`, `gender`, `class_grade`, `status`

## Project Structure

- `main.py` - entry point for the application
- `utils.py` - helper input validation utilities
- `data/` - CSV storage and data loading/saving modules
- `applicant/` - applicant workflow modules
- `student/` - student workflow modules
- `parent/` - parent workflow modules
- `teacher/` - teacher workflow modules
- `principal/` - principal workflow modules

## Notes

- The application uses CSV files as the backend, so data is persisted across runs if the files are saved.
- The system is designed for simple CLI interaction and sample school management functionality.
- To reset the sample dataset, re-run `python data/fill_data.py`.
