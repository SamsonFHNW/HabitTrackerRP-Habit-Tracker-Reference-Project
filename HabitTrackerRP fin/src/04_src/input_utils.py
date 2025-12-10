# src/input_utils.py
def ask_nonempty(prompt):
    """Prompt until the user provides non-empty input."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


def ask_choice(label, options):
    """Prompt until the user enters one of the allowed options (case-insensitive)."""
    options_lower = [o.lower() for o in options]
    while True:
        value = input(f"{label} {options}: ").strip().lower()
        if value in options_lower:
            return value
        print(f"Please enter one of: {', '.join(options)}.")