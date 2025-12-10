#  HabitTrackerRP — Habit Tracking Console Application
*A reference project for the Programming Foundations module (FHNW, BSc BIT)*

HabitTrackerRP is a small but complete console-based Python application designed to help users track daily and weekly habits.  
Although simple in appearance, the project demonstrates core programming concepts such as modular design, input validation, date-based logic, CSV data persistence, and the use of pure Python standard libraries.


---

# 1.  Project Overview

HabitTrackerRP enables users to manage personal habits such as *reading*, *exercising*, or *practicing a skill*.  
The program uses a textual menu to interact with the user and stores all data inside a `habits.csv` file so that progress is saved between sessions.

### **What the program supports**
- Adding new habits  
- Marking habits as done  
- Automatically resetting habit statuses (daily/weekly)  
- Viewing all habits in a formatted table  
- Filtering habits by status or frequency  
- Deleting habits  
- Persistent habit storage using CSV  

This offers an ideal learning environment: the program is small enough to understand in one semester, yet rich enough to show how real applications maintain state and apply logic over time.

---

# 2.  Analysis

## 2.1 The Problem  
People often struggle to maintain consistency in their routines. Without a tracking system, it's easy to lose motivation or forget progress.  
For example:  
- Did I drink enough water today?  
- Did I practice piano this week?  
- Have I exercised regularly?  

While many sophisticated habit apps exist, they are often too complex for beginners to understand or too bloated for simple tasks. Students need a system that is both **practical and easy to study**.

## 2.2 Scenario  
HabitTrackerRP provides users with a lightweight console tool to manage basic habits.  
It focuses on clarity and simplicity:  
- A user enters habits they want to track  
- The system remembers them through a CSV file  
- Each time the program starts, it automatically updates which habits are marked as *done* or *pending* based on date information  
- Users can complete habits, filter them for readability, and delete them as needed  

This scenario is realistic for a real beginner software tool: clear functionality, predictable behavior, and transparent data storage.

---

# 3.  User Stories

HabitTrackerRP was designed with the following user stories in mind:

- **As a user, I want to add a habit with a meaningful description so that I know what to complete.**  
- **As a user, I want habits to start as “pending” so I know which tasks are still open.**  
- **As a user, I want to mark a habit as done to track my progress.**  
- **As a user, I want the system to automatically update habits based on the date so I don’t have to reset them myself.**  
- **As a user, I want to see all my habits in a readable format.**  
- **As a user, I want to filter habits by status or frequency so I can focus on relevant ones.**  
- **As a user, I want my data saved so that progress is preserved between program runs.**

These user stories guided the design of the system and its required functionality.

---

# 4.  Solution Design

### 4.1 Main Use Cases  

---

###  **Add Habit**

#### Relevant snippet:
```python
habits.append(
    {
        "id": str(next_id(habits)),
        "description": ask_nonempty("Description: "),
        "frequency": ask_choice("Frequency", FREQUENCIES),
        "created_date": today_str(),
        "status": "pending",
        "completed_date": "",
        "completion_history": "",
    }
)
```

---

###  **Mark Habit as Done**

#### Relevant snippet:
```python
for h in habits:
    if h["id"] == habit_id:
        h["status"] = "done"
        h["completed_date"] = today
        append_completion_to_history(h, today)
```

---

###  **Automatic Daily/Weekly Reset**

#### Relevant snippet:
```python
if h["frequency"] == "daily":
    h["status"] = "done" if last == today else "pending"
else:
    last_week = week_code_from_date(last)
    h["status"] = "done" if last_week == current_week else "pending"
```

---

###  **Delete Habit**

#### Relevant snippet:
```python
habits = [h for h in habits if h["id"] != habit_id]
```

---

###  **Filter Habits**

#### Relevant snippet:
```python
if choice == "1":
    status = ask_choice("Status", STATUSES)
    result = [h for h in habits if h["status"] == status]
```

---

# 5.  Input Validation

### Non-empty input
```python
def ask_nonempty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")
```

### Choice validation
```python
def ask_choice(label, options):
    value = input(f"{label} {options}: ").strip().lower()
```

### ID validation
```python
if not habit_id.isdigit():
    print("ID must be a number.")
    return
```

---

# 6.  File Handling & Persistence

### File Creation
```python
if not os.path.exists(DATA_FILE):
    csv.DictWriter(f, FIELDS).writeheader()
```

### Loading data
```python
return list(csv.DictReader(f))
```

### Saving data
```python
writer.writeheader()
writer.writerows(habits)
```

---

# 7.  Program Flow

1. `ensure_file()` creates the CSV if missing  
2. `load_habits()` reads all habits  
3. `refresh_statuses()` updates each habit  
4. `save_habits()` writes updated statuses back  
5. Menu options allow the user to interact with the data  
6. Loop continues until user selects exit  

---

# 8.  Repository Structure

```
HabitTrackerRP/Additionals
└── src/
    ├── main.py             # main console program
    ├── input_utils.py      # validated input handling
    ├── output_utils.py     # formatted habit display
    ├── storage.py          # CSV file read/write
    ├── processing.py       # habit logic (reset and history)
    └── id_utils.py         # next ID generator

# Or

HabitTrackerRP/
│
├── habits.csv              # persistent habit storage
│
├── HabitTrackerRP          # main program
│
└── README.md               # project documentation

```

# 9.  Conclusion

HabitTrackerRP is a well-rounded introductory project that teaches:

- modular programming  
- user interaction  
- robust input handling  
- CSV data storage  
- date-based logic  
- basic software documentation  