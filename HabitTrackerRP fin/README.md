# 📘 HabitTrackerRP – Habit Tracker Reference Project (Console)

This project is a reference implementation for the **Programming Foundations** module.  
It demonstrates how to design, implement, structure, and document a small console-based Python application using user interaction, data validation, and file processing.

HabitTrackerRP enables users to manage simple personal habits by adding tasks, updating their completion status, filtering habits, or removing habits they no longer need. All habits are stored persistently in a CSV file.

---

# 1. 🎯 Project Goal

The goals of HabitTrackerRP are to:

- Guide students through the complete workflow from **analysis to implementation**  
- Reinforce Python fundamentals: functions, loops, conditionals, data structures  
- Demonstrate **file processing** and **data persistence** using CSV  
- Develop a user-friendly **console interaction** flow  
- Produce clean, well-structured, and maintainable code  
- Prepare students for more advanced projects in later modules  

---

# 2. 🧩 Problem Analysis

### Problem  

People often struggle to keep track of daily or weekly habits (e.g., drinking water, exercising, reading).  
Without a proper system, habits are quickly forgotten, making it difficult to stay consistent and motivated.

### Scenario  

HabitTrackerRP provides a simple and lightweight solution that allows users to track their habits using a console-based application.

The system stores each habit with:

- an **ID**
- a **description**
- a **frequency** (`daily` or `weekly`)
- an automatically assigned **created date**
- a **status** (`pending` or `done`)
- an automatically assigned **completed date** (last time it was done)
- a **completion history** listing all dates when the habit was completed

Additionally, the application automatically resets the status based on time:

- For **daily habits**:  
  - If the last completed date is **today**, status remains `done`.  
  - Otherwise, status becomes `pending`.

- For **weekly habits**:  
  - If the last completed date is in the **current calendar week**, status remains `done`.  
  - Otherwise, status becomes `pending`.

This allows users to see both their current tasks (pending/done for the current period) and their completion history over time.

---

# 3. 👤 User Stories

- *As a user, I want to add new habits so I can keep track of what I want to achieve.*
- *As a user, I want habits to automatically start with a pending status so I do not need to manage states manually.*
- *As a user, I want to mark habits as done so I can see what I already completed.*
- *As a user, I want the program to automatically record when a habit was created and last completed.*
- *As a user, I want to see a history of all dates when I completed a habit.*
- *As a user, I want to filter habits by status or frequency to quickly see what is pending or done.*
- *As a user, I want my habits to be saved between sessions so I don’t lose progress.*

---

# 4. 🧪 Use Cases

### Add Habit  
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

Filtered results are displayed in the same formatted table.

---

# 5. 🛠 Project Requirements

### 1. Console Interaction  

The application must provide an interactive menu where users can:

- add habits  
- mark habits as done  
- delete habits  
- view all habits  
- filter habits by status or frequency  
- exit the program  

### 2. Input Validation  

The program validates all user input:

- Description must not be empty  
- Frequency must be `daily` or `weekly`  
- Status (for filtering) must be `pending` or `done`  
- ID must be a valid integer that exists (for marking done or deleting)  
- Menu options must be valid choices  

No invalid input should cause crashes.

### 3. File Processing  

- All habits are stored in **habits.csv**  
- The CSV file is created automatically if missing  
- The CSV includes the following headers:

```text
id,description,frequency,created_date,status,completed_date,completion_history
