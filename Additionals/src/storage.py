# src/storage.py
import csv
import os

FIELDS = [
    "id",
    "description",
    "frequency",
    "created_date",
    "status",
    "completed_date",
    "completion_history",
]

DATA_FILE = "habits.csv"


def ensure_file():
    """Create CSV file with headers when it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, FIELDS).writeheader()


def load_habits():
    """Load all habits from CSV and return list of dicts."""
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_habits(habits):
    """Save updated habits to CSV using canonical FIELDS order."""
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, FIELDS)
        writer.writeheader()
        writer.writerows(habits)