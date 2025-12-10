# src/processing.py
from datetime import datetime

FREQUENCIES = ["daily", "weekly"]
STATUSES = ["pending", "done"]


def today_str():
    return datetime.today().strftime("%Y-%m-%d")


def current_week_code():
    year, week, _ = datetime.today().isocalendar()
    return f"{year}-W{week:02d}"


def week_code_from_date(date_str):
    """Convert 'YYYY-MM-DD' -> 'YYYY-Www' week code."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    year, week, _ = dt.isocalendar()
    return f"{year}-W{week:02d}"


def append_completion_to_history(habit, date_str):
    """
    Append date_str to habit['completion_history'] only if it's not already the last entry.
    Preserves '|' separated format, returns the updated habit dict (mutates in place).
    """
    history = habit.get("completion_history", "").strip()
    if history:
        parts = history.split("|")
        if parts[-1] != date_str:
            history = history + "|" + date_str
    else:
        history = date_str
    habit["completion_history"] = history
    return habit


def refresh_statuses(habits):
    """Update each habit['status'] to done/pending based on completed_date and frequency."""
    today = today_str()
    current_week = current_week_code()
    for h in habits:
        last = h.get("completed_date", "").strip()
        if not last:
            h["status"] = "pending"
            continue
        if h["frequency"] == "daily":
            h["status"] = "done" if last == today else "pending"
        else:
            last_week = week_code_from_date(last)
            h["status"] = "done" if last_week == current_week else "pending"
    return habits