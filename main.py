from cli import run_CLI
from todo_list import ToDoList

if __name__ == "__main__":
    todo = ToDoList("tasks.json")
    run_CLI(todo)
