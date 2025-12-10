# src/id_utils.py

def next_id(habits):
    """Return next numeric id (as int)."""
    return 1 + max([int(h["id"]) for h in habits], default=0)