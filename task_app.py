#!/usr/bin/env python3
"""Приложение учета задач."""
import json
import sys

DEFAULT_PRIORITY = "normal"
DATA_FILE = "tasks.json"

def load_tasks(path=DATA_FILE):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks, path=DATA_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "priority": DEFAULT_PRIORITY, "done": False})
    save_tasks(tasks)

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def filter_by_status(tasks, done):
    return [t for t in tasks if t.get("done", False) == done]


VALID_PRIORITIES = {"low", "normal", "high"}

def validate_priority(value):
    if value not in VALID_PRIORITIES:
        raise ValueError(f"invalid priority: {value}")
    return value

PRIORITY_ORDER = {"high": 0, "normal": 1, "low": 2}

def sort_tasks(tasks):
    return sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t.get("priority", "normal"), 1))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: task_app.py add <title>")
        sys.exit(1)
    if sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
        print("task added")