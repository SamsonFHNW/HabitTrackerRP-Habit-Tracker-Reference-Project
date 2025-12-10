# 📘 HabitTrackerRP

This project is a reference implementation for the **Programming Foundations** module.  
It demonstrates how to design, implement, structure, and document a small console-based Python application using user interaction, data validation, and file processing.

HabitTrackerRP enables users to manage simple personal habits by adding tasks, updating their completion status, filtering habits, or removing habits they no longer need. All habits are stored persistently in a CSV file.

---

1. 🌱 HabitTrackerRP – Habit Tracker Reference Project (Console)

This project is created for the course Programming Foundations (FHNW, BSc BIT).
Project Goal

The goals of HabitTrackerRP are to:

- Guide students through the complete workflow from **analysis to implementation**  
- Reinforce Python fundamentals: functions, loops, conditionals, data structures  
- Demonstrate **file processing** and **data persistence** using CSV  
- Develop a user-friendly **console interaction** flow  
- Produce clean, well-structured, and maintainable code  
- Prepare students for more advanced projects in later modules 

HabitTrackerRP allows users to manage daily or weekly habits by adding them, marking them as completed, filtering them, and removing them. All habits are saved in a CSV file so their progress is persistent across sessions.

⸻

2. 📝 Analysis

Problem

People often struggle to keep track of personal habits such as reading, exercising, or drinking enough water. Without a simple system, habits are easily forgotten, making it difficult to stay consistent and motivated.

Scenario

## HabitTrackerRP supports users by providing a small console-based tool where they can:
	•	add new habits
	•	track which habits are done or pending
	•	automatically reset habits based on time (daily or weekly)
	•	store their data persistently

## The application updates habit status automatically:
	•	Daily habits reset each day
	•	Weekly habits reset each calendar week (ISO week number)

This helps users stay aware of what they need to complete for the current day or week.

## User Stories
	•	As a user, I want to add habits with meaningful descriptions.
	•	As a user, I want habits to be marked as pending when created.
	•	As a user, I want to mark habits as done so I can track my progress.
	•	As a user, I want the system to automatically update habit status based on the date.
	•	As a user, I want to view all my habits in an easy-to-read table.
	•	As a user, I want to filter habits by status or frequency.
	•	As a user, I want my habit data saved between program runs.


⸻

3. ✅ Project Requirements:

Interactive App (Console Input):

## The application interacts with the user through a console menu.
HabitTrackerRP
1) Add habit
2) Mark habit as done
3) Delete habit
4) View all habits
5) Filter habits
6) Exit
""")
choice = input("Select 1-6: ").strip()

Use Cases:

## Add Habit  
User enters a description and selects whether the habit is daily or weekly.  
System automatically sets:

- `status = pending`  
- `created_date = today`  
- `completed_date = ""`  
- `completion_history = ""`  

### Mark Habit as Done  
User selects a habit by ID.  
System:

- sets `status = done`  
- sets `completed_date = today`  
- appends `today` to `completion_history` (e.g. `2025-01-21|2025-01-22`)  

### Automatic Status Reset (on application start)  
When the application starts, it loads all habits and updates their status:

- For **daily** habits:
  - if `completed_date == today` → status stays `done`
  - otherwise → status becomes `pending`

- For **weekly** habits:
  - if `completed_date` is in the same ISO week as today → status stays `done`
  - otherwise → status becomes `pending`

Updated statuses are then saved back to the CSV file.

### Delete Habit  
User selects a habit by ID.  
System removes the habit from the CSV file.

### View All Habits  
System displays all habits in a formatted table with:

- ID  
- Frequency  
- Created date  
- Status (pending/done for current period)  
- Last completed date  
- Completion history (all completion dates, separated by `|`)  
- Description  

### Filter Habits  
User can filter habits by:

- **Status** (pending/done)  
- **Frequency** (daily/weekly)  

4.  Data Validation

All user input is validated to prevent crashes and ensure correct data.

## Non-empty input

def ask_nonempty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")

## Choice validation

def ask_choice(label, options):
    options_lower = [o.lower() for o in options]
    while True:
        value = input(f"{label} {options}: ").strip().lower()
        if value in options_lower:
            return value
        print(f"Please enter one of: {', '.join(options)}.")

## Habit ID validation


habit_id = ask_nonempty("Enter habit ID to mark as done: ")
if not habit_id.isdigit():
    print("ID must be a number.")
    return

5. File Processing

The application reads and writes all habit data using a CSV file named habits.csv.

## Creating the file if missing:

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, FIELDS).writeheader()

## Loading CSV:
with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
    return list(csv.DictReader(f))

## Saving CSV:

with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, FIELDS)
    writer.writeheader()
    writer.writerows(habits)

# Example habits.csv entry

1,Read book,daily,2025-01-14,done,2025-01-18,2025-01-14|2025-01-18

6. Core Logic

Automatic Daily/Weekly Reset

# From processing.py:

   if h["frequency"] == "daily":
       h["status"] = "done" if last == today else "pending"
   else:
       last_week = week_code_from_date(last)
       h["status"] = "done" if last_week == current_week else "pending"

# Marking Habit as Done
     h["status"] = "done"
     h["completed_date"] = today
     append_completion_to_history(h, today)

# Adding Completion History
     if parts[-1] != date_str:
          history = history + "|" + date_str


# Deleting a Habit
    habits = [h for h in habits if h["id"] != habit_id]

# Filtering Habits
    result = [h for h in habits if h["frequency"] == freq]

# or:
    result = [h for h in habits if h["status"] == status]


8. 📂 Repository Structure

HabitTrackerRP/Additionals
└── src/
    ├── main.py             # main console program
    ├── input_utils.py      # validated input handling
    ├── output_utils.py     # formatted habit display
    ├── storage.py          # CSV file read/write
    ├── processing.py       # habit logic (reset and history)
    └── id_utils.py         # next ID generator

# OR

HabitTrackerRP/
│
├── habits.csv              # persistent habit storage
│
├── HabitTrackerRP          # main program
│
└── README.md               # project documentation


Each module handles one responsibility, keeping the code clear and maintainable.

9. 🏁 Conclusion

HabitTrackerRP is a complete and well-structured example of a Python console application.
It demonstrates all required aspects of the Programming Foundations module:
	•	user interaction
	•	input validation
	•	file handling
	•	modular code organization
	•	practical logic (daily/weekly habits)

The system is simple yet functional, easy to extend, and well aligned with the course learning goals.



