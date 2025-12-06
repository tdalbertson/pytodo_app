# Changelog
All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**  
and this project adheres to **Semantic Versioning**.

---

## [Unreleased]
### Added
- Placeholder for upcoming features and improvements.

---

## [v1.1.0] - 2025-12-05
### Added
- Implemented tracking of `used_ids` and `available_ids` in `ToDoList` to manage task IDs more intelligently.
- Integrated ID tracking into `add_task` and `delete_task` so new tasks can reuse IDs from deleted tasks when available.

### Changed
- Renamed `remove_task` to `delete_task` throughout the codebase for clearer, more consistent API naming.
- Updated CLI logic to use the new `delete_task` method name.

---

## [v1.0.0] - 2025-12-05
### Added
- Initial stable release of the Task CLI on the `main` branch.
- Command-line interface to manage tasks interactively.
- Core commands:
  - `add` – Add a new task.
  - `update` – Update an existing task’s description.
  - `delete` – Remove a task by ID with confirmation.
  - `mark-todo`, `mark-in-progress`, `mark-done` – Change task status.
  - `list` – Show all tasks or filter by status.
  - `exit` – Exit the application with confirmation.

### Changed
- Converted command names and statuses to Enums (`Command`, `Status`) for safer, centralized command/status handling.  
  _(Commit: `bddce9f` – “Convert commands and statuses to Enum”)_
- Tweaked `list_tasks` behavior and messages to:
  - Use a newline for the “no tasks found for status” message.
  - Improve the message shown when the tasks list is empty.  
  _(Commits: `e0e8156`, `ef4107b`)_
- Removed a redundant confirmation message from the `add` command, reducing noise in the CLI.  
  _(Commit: `4e3645e` – “Remove redundant confirmation message from add command”)_

### Documentation
- Added the project URL to the README and moved it to the top for better visibility.  
  _(Commits: `75afabc`, `7308e8a`, `96d0e54`)_
- Updated command syntax examples in the README for clarity.  
  _(Commit: `0a5308e`)_

---
