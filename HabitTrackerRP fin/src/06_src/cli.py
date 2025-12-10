# src/cli.py
from src.storage import ensure_file, load_habits, save_habits
from src.processing import refresh_statuses, today_str, append_completion_to_history
from src.input_utils import ask_nonempty, ask_choice
from src.output_utils import show_habits
from src.id_utils import next_id
from src.processing import FREQUENCIES, STATUSES

def add_habit():
    habits = load_habits()
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
    save_habits(habits)
    print("Habit added.")


def change_status_to_done():
    habits = refresh_statuses(load_habits())
    save_habits(habits)
    show_habits(habits)
    if not habits:
        return
    habit_id = ask_nonempty("Enter habit ID to mark as done: ")
    if not habit_id.isdigit():
        print("ID must be a number.")
        return
    today = today_str()
    found = False
    for h in habits:
        if h["id"] == habit_id:
            h["status"] = "done"
            h["completed_date"] = today
            append_completion_to_history(h, today)
            found = True
            break
    if not found:
        print("No habit with that ID.")
        return
    save_habits(habits)
    print(f"Habit {habit_id} marked as done.")


def remove_habit():
    habits = load_habits()
    show_habits(habits)
    if not habits:
        return
    habit_id = ask_nonempty("Enter habit ID to delete: ")
    before = len(habits)
    habits = [h for h in habits if h["id"] != habit_id]
    if len(habits) == before:
        print("No habit with that ID.")
        return
    save_habits(habits)
    print("Habit deleted.")


def filter_habits():
    habits = refresh_statuses(load_habits())
    save_habits(habits)
    if not habits:
        print("No habits to filter.")
        return
    print("Filter by: 1=status 2=frequency")
    choice = input("Choice: ").strip()
    if choice == "1":
        status = ask_choice("Status", STATUSES)
        result = [h for h in habits if h["status"] == status]
    elif choice == "2":
        freq = ask_choice("Frequency", FREQUENCIES)
        result = [h for h in habits if h["frequency"] == freq]
    else:
        print("Invalid choice.")
        return
    show_habits(result)


def main():
    ensure_file()
    habits = refresh_statuses(load_habits())
    save_habits(habits)
    while True:
        print(
            """
HabitTrackerRP
1) Add habit
2) Mark habit as done
3) Delete habit
4) View all habits
5) Filter habits
6) Exit
"""
        )
        choice = input("Select 1-6: ").strip()
        if choice == "1":
            add_habit()
        elif choice == "2":
            change_status_to_done()
        elif choice == "3":
            remove_habit()
        elif choice == "4":
            show_habits(load_habits())
        elif choice == "5":
            filter_habits()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()