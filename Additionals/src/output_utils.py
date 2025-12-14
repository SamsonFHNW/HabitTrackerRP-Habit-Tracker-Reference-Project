# src/output_utils.py
def show_habits(habits):
    if not habits:
        print("No habits found.")
        return

    header = (
        f"{'ID':<3} | "
        f"{'Freq':<6} | "
        f"{'Created':<10} | "
        f"{'Status':<7} | "
        f"{'LastDone':<10} | "
        f"{'History':<20} | "
        f"Description"
    )
    print(header)
    print("-" * len(header))

    for h in habits:
        history = h.get("completion_history", "")
        print(
            f"{h['id']:<3} | "
            f"{h['frequency']:<6} | "
            f"{h['created_date']:<10} | "
            f"{h['status']:<7} | "
            f"{h['completed_date']:<10} | "
            f"{history:<20} | "
            f"{h['description']}"
        )