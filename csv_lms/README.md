# README for the Python LMS Program

## Overview

This Python program is a simple Learning Management System (LMS) for managing students' data. It allows users to add students, view student records, calculate averages, and check pass/fail statuses.

## Features

1. **Add Student**: Save a student's name and grades for Math, Science, and English into a CSV file.
2. **View All Students**: Display all student records stored in the CSV file.
3. **Calculate Student's Average**: Compute the average marks of a specific student.
4. **Calculate Class Average**: Compute the average marks of all students in the class.
5. **Check Individual Pass/Fail Status**: Check whether a specific student has passed or failed based on their grades.
6. **Check Class Pass/Fail Status**: Determine whether the entire class passed or failed based on average marks.
7. **Quit**: Exit the program.

## Usage Instructions

1. Run the program by executing the Python file:
   ```bash
   python main.py
   ```
2. Follow the menu options displayed in the terminal:
   - Enter `1` to add a new student.
   - Enter `2` to view all available student records.
   - Enter `3` to check the average marks of a specific student.
   - Enter `4` to calculate the average marks for the entire class.
   - Enter `5` to check the pass/fail status of a specific student.
   - Enter `6` to check the pass/fail status of the entire class.
   - Enter `7` to quit the program.

## File Structure

- **students.csv**: A file where student data is saved. This file is created automatically if it doesn't exist.

## How It Works

1. **Data Validation**:
   - Names must be unique and alphabetic.
   - Grades must be integers between 0 and 100.
2. **Data Storage**:
   - Student data is stored in a CSV file (`students.csv`).
3. **Menu Options**:
   - Each menu option triggers a specific functionality, interacting with the data as needed.

## Notes

- If the CSV file is deleted or empty, the program handles it gracefully and allows you to add new students.
- Students who score less than 40 in any subject are considered to have failed that subject.
- Average marks below 40 for the entire class result in the class being marked as "failed."
