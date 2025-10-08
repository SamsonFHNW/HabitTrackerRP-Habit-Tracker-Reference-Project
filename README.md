HabitTrackerRP – Habit Tracker Reference Project (Console)

🚧 This is a template repository for student project in the course Programming Foundations at FHNW, BSc BIT.
🚧 Do not keep this section in your final submission.

This project is intended to:
	•	Practice the complete process from problem analysis to implementation
	•	Apply basic Python programming concepts learned in the Programming Foundations module
	•	Demonstrate the use of console interaction, data validation, and file processing
	•	Produce clean, well-structured, and documented code
	•	Prepare students for teamwork and documentation in later modules

⸻

📝 Analysis

Problem

In daily life, people often struggle to stay consistent with habits or keep track of small tasks. Many write them on paper or keep them in their memory, which leads to missed tasks, forgotten goals, and lack of motivation.

Scenario

HabitTrackerRP helps users manage their personal tasks and habits through a simple console-based application. The user can add new tasks, mark them as completed, delete tasks they no longer need, and filter tasks by description, status, or priority. The system stores tasks in a file so that progress is not lost between sessions. The habits should always be assigned to a date.

User Stories
	•	As a user, I want to add new tasks with a description and priority.
	•	As a user, I want to remove tasks I no longer need.
	•	As a user, I want to mark tasks as completed.
	•	As a user, I want to view all my tasks.
	•	As a user, I want to filter tasks by description, status, or priority.
	•	As a user, I want my tasks to be saved automatically so i can continue later

Use Cases
	•	Add Task (append new task to the file with description, priority, and status = pending)
	•	Remove Task (delete a specific task by ID or name)
	•	Mark Task Completed (change status in the file to “done”)
	•	Show Tasks (list all tasks with ID, description, status, and priority)
	•	Filter Tasks (list tasks based on description keywords, completion status, or priority)

⸻

✅ Project Requirements

1. Interactive App (Console Input)

The application interacts with the user via the console. Users can:
	•	Add new tasks
	•	Remove tasks
	•	Mark tasks as completed
	•	View all tasks
	•	Filter tasks by description, status, or priority

2. Data Validation

The application validates user input to ensure correctness:
	•	Task description cannot be empty.
	•	Priority must be one of: Low, Medium, High.
	•	When selecting a task by ID, the input must be a valid number corresponding to an existing task.
	•	Main menu only accepts valid options.


	Test
