# oop/tracker_oop.py
import csv
import os
from datetime import datetime

DATA_FILE = "habits.csv"
FIELDS = [
    "id",
    "description",
    "frequency",
    "created_date",
    "status",
    "completed_date",
    "completion_history",
]
FREQUENCIES = ["daily", "weekly"]
STATUSES = ["pending", "done"]


class Habit:
    def __init__(self, id_, description, frequency, created_date, status="pending",
                 completed_date="", completion_history=""):
        self.id = str(id_)
        self.description = description
        self.frequency = frequency
        self.created_date = created_date
        self.status = status
        self.completed_date = completed_date
        self.completion_history = completion_history

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "frequency": self.frequency,
            "created_date": self.created_date,
            "status": self.status,
            "completed_date": self.completed_date,
            "completion_history": self.completion_history,
        }


class HabitTracker:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.ensure_file()
        self.habits = self.load_habits()
        self.refresh_statuses()
        self.save_habits()

    def ensure_file(self):
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w", newline="", encoding="utf-8") as f:
                csv.DictWriter(f, FIELDS).writeheader()

    def load_habits(self):
        with open(self.data_file, "r", newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        return [self._dict_to_habit(r) for r in rows]

    def save_habits(self):
        with open(self.data_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, FIELDS)
            writer.writeheader()
            writer.writerows([h.to_dict() for h in self.habits])

    def _dict_to_habit(self, d):
        return Habit(
            id_=d["id"],
            description=d["description"],
            frequency=d["frequency"],
            created_date=d["created_date"],
            status=d.get("status", "pending"),
            completed_date=d.get("completed_date", ""),
            completion_history=d.get("completion_history", ""),
        )

    @staticmethod
    def today_str():
        return datetime.today().strftime("%Y-%m-%d")

    @staticmethod
    def current_week_code():
        y, w, _ = datetime.today().isocalendar()
        return f"{y}-W{w:02d}"

    @staticmethod
    def week_code_from_date(date_str):
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        y, w, _ = dt.isocalendar()
        return f"{y}-W{w:02d}"

    def refresh_statuses(self):
        today = self.today_str()
        current_week = self.current_week_code()
        for h in self.habits:
            last = h.completed_date.strip()
            if not last:
                h.status = "pending"
                continue
            if h.frequency == "daily":
                h.status = "done" if last == today else "pending"
            else:
                last_week = self.week_code_from_date(last)
                h.status = "done" if last_week == current_week else "pending"

    def next_id(self):
        return 1 + max([int(h.id) for h in self.habits], default=0)

    def append_completion_to_history(self, habit, date_str):
        history = habit.completion_history.strip()
        if history:
            parts = history.split("|")
            if parts[-1] != date_str:
                history = history + "|" + date_str
        else:
            history = date_str
        habit.completion_history = history

    def add_habit(self, description, frequency):
        h = Habit(
            id_=self.next_id(),
            description=description,
            frequency=frequency,
            created_date=self.today_str(),
            status="pending",
            completed_date="",
            completion_history="",
        )
        self.habits.append(h)
        self.save_habits()

    def mark_done_by_id(self, habit_id):
        today = self.today_str()
        found = False
        for h in self.habits:
            if h.id == str(habit_id):
                h.status = "done"
                h.completed_date = today
                self.append_completion_to_history(h, today)
                found = True
                break
        if found:
            self.save_habits()
        return found

    def remove_by_id(self, habit_id):
        before = len(self.habits)
        self.habits = [h for h in self.habits if h.id != str(habit_id)]
        if len(self.habits) != before:
            self.save_habits()
            return True
        return False

    def filter_by_status(self, status):
        return [h for h in self.habits if h.status == status]

    def filter_by_frequency(self, freq):
        return [h for h in self.habits if h.frequency == freq]

    def show_habits(self, list_to_show=None):
        if list_to_show is None:
            list_to_show = self.habits
        if not list_to_show:
            print("No habits found.")
            return
        print(
            f"{'ID':<3} {'Freq':<7} {'Created':<10} "
            f"{'Status':<7} {'LastDone':<10} History | Description"
        )
        print("-" * 100)
        for h in list_to_show:
            print(
                f"{h.id:<3} {h.frequency:<7} {h.created_date:<10} "
                f"{h.status:<7} {h.completed_date:<10} "
                f"{h.completion_history} | {h.description}"
            )


def run_cli():
    tracker = HabitTracker()
    while True:
        print(
            """
HabitTrackerRP (OOP)
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
            desc = input("Description: ").strip()
            freq = input(f"Frequency {FREQUENCIES}: ").strip().lower()
            tracker.add_habit(desc, freq)
            print("Habit added.")
        elif choice == "2":
            tracker.refresh_statuses()
            tracker.save_habits()
            tracker.show_habits()
            hid = input("Enter habit ID to mark as done: ").strip()
            if not hid.isdigit():
                print("ID must be a number.")
            elif tracker.mark_done_by_id(hid):
                print(f"Habit {hid} marked as done.")
            else:
                print("No habit with that ID.")
        elif choice == "3":
            tracker.show_habits()
            hid = input("Enter habit ID to delete: ").strip()
            if tracker.remove_by_id(hid):
                print("Habit deleted.")
            else:
                print("No habit with that ID.")
        elif choice == "4":
            tracker.show_habits()
        elif choice == "5":
            tracker.refresh_statuses()
            tracker.save_habits()
            print("Filter by: 1=status 2=frequency")
            ch = input("Choice: ").strip()
            if ch == "1":
                st = input(f"Status {STATUSES}: ").strip().lower()
                tracker.show_habits(tracker.filter_by_status(st))
            elif ch == "2":
                fq = input(f"Frequency {FREQUENCIES}: ").strip().lower()
                tracker.show_habits(tracker.filter_by_frequency(fq))
            else:
                print("Invalid choice.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_cli()