https://github.com/tdalbertson/pytodo_app

# py_todo_app

Simple CLI to-do list written in Python. Tasks are stored in `tasks.json` so they persist between runs.

## Requirements
- Python 3.10+

## Install & Run
```bash
python3 main.py
```
You will see the prompt `task-cli`. Type commands there.

## Commands
- `add Buy groceries` — add a task.
- `update 1 Buy groceries and cook dinner` — change description by ID.
- `delete 1` — remove a task (asks for confirmation).
- `mark-todo 1` / `mark-in-progress 1` / `mark-done 1` — change status.
- `list` — show all tasks.
- `exit` — quit (asks for confirmation).

## Data
- Tasks live in `tasks.json` in the project root.
- Existing timestamps/status from the file are preserved when the app loads.
- Tasks are saved to `tasks.json` when you exit the CLI (after you confirm `exit`). Work in progress is kept in memory until then.
