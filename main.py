from cli import run_CLI
from todo_list import ToDoList

if __name__ == "__main__":
    todo = ToDoList("tasks.json")
    run_CLI(todo)

    # Write existing tasks once exiting from the tasks CLI
    todo.write_tasks_to_file()
