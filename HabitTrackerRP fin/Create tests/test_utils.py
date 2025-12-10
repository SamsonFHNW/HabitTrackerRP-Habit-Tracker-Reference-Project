# tests/test_utils.py
import tempfile
import os
from src.processing import week_code_from_date, append_completion_to_history, refresh_statuses, today_str
from src.id_utils import next_id

def test_week_code_from_date():
    assert week_code_from_date("2025-01-01").startswith("2025-W")
    assert week_code_from_date("2020-12-31").startswith("2020-W")

def test_append_completion_to_history_new():
    h = {"completion_history": ""}
    append_completion_to_history(h, "2025-12-09")
    assert h["completion_history"] == "2025-12-09"

def test_append_completion_to_history_append():
    h = {"completion_history": "2025-12-08"}
    append_completion_to_history(h, "2025-12-09")
    assert h["completion_history"] == "2025-12-08|2025-12-09"

def test_append_completion_to_history_no_dup():
    h = {"completion_history": "2025-12-09"}
    append_completion_to_history(h, "2025-12-09")
    assert h["completion_history"] == "2025-12-09"

def test_next_id():
    habits = [{"id": "1"}, {"id": "2"}, {"id": "10"}]
    assert next_id(habits) == 11