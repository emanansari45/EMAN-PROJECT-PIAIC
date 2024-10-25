# Student Performance Tracker

A Python-based tool for tracking and analyzing student academic performance across multiple subjects.

## Features

- Add Student: Enter student names and scores for Math, Science, and English
- View Data: Display all stored student information
- Performance Summary: Calculate individual and class averages
- Status Tracking: Automatically determine if students are passing or need improvement

## Requirements

- Python 3.x
- statistics library (included in Python standard library)

## Installation

1. Clone this repository:
bash
git clone https://github.com/emanansari45/student-performance-tracker.git


2. Navigate to the project directory:
bash
cd student-performance-tracker


3. Run the script:
bash
python emanasghar.py


## Usage

### Menu Options

1. Add a Student
   - Enter student name
   - Input scores for Math, Science, and English (0-100)

2. View Stored Data
   - See all student records
   - View individual subject scores

3. Display Performance Summary
   - Individual student averages
   - Passing status
   - Overall class average

4. Quit
   - Exit the program

### Example Usage


Options:
1. Add a student
2. View stored data
3. Display performance summary
4. Quit

Enter your choice (1-4): 1
Enter student name: Alice
Enter score for Math: 85
Enter score for Science: 78
Enter score for English: 92
Added Alice to the system.


## Technical Details

### Structure

- Student class: Manages individual student data
- PerformanceTracker class: Handles overall data management
- Command-line interface for user interaction

### Scoring System

- Scores must be between 0 and 100
- Passing threshold: 40 points
- Status categories:
  - "Passing": Average score ≥ 40
  - "Need Improvement": Average score < 40

## Error Handling

- Validates score range (0-100)
- Ensures valid numeric inputs
- Prevents duplicate student entries
