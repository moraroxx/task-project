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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: task_app.py add <title>")
        sys.exit(1)
    if sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
        print("task added")