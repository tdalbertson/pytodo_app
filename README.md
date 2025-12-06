# py_todo_app

Simple CLI to-do list written in Python. Tasks are stored in `tasks.json` so they persist between runs.

## Task Tracker Project URL
https://roadmap.sh/projects/task-tracker

## Requirements
- Python 3.10+

## Install & Run
```bash
python3 main.py
```
You will see the prompt `task-cli`. Type commands there.

## Commands
- `add Buy groceries` — add a task.
- `update {task_id} Buy groceries and cook dinner` — change description by ID.
- `delete {task_id}` — remove a task (asks for confirmation).
- `mark-todo {task_id}` / `mark-in-progress {task_id}` / `mark-done {task_id}` — change status.
- `list` — show all tasks.
- `exit` — quit (asks for confirmation).

## Data
- Tasks live in `tasks.json` in the project root.
- Existing timestamps/status from the file are preserved when the app loads.
- Tasks are saved to `tasks.json` when you exit the CLI (after you confirm `exit`). Work in progress is kept in memory until then.

## Versioning
This project uses **Semantic Versioning** for release management.

- **Latest stable release:** `v1.1.0`
- All release notes are available in the **[CHANGELOG](CHANGELOG.md)**.
- Older versions can be accessed through Git tags in this repository.