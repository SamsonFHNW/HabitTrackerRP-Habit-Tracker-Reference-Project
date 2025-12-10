# src/output_utils.py
def show_habits(habits):
    """Print a compact table view of habits."""
    if not habits:
        print("No habits found.")
        return

    print(
        f"{'ID':<3} {'Freq':<7} {'Created':<10} "
        f"{'Status':<7} {'LastDone':<10} History | Description"
    )
    print("-" * 100)
    for h in habits:
        history = h.get("completion_history", "")
        print(
            f"{h['id']:<3} {h['frequency']:<7} {h['created_date']:<10} "
            f"{h['status']:<7} {h['completed_date']:<10} "
            f"{history} | {h['description']}"
        )