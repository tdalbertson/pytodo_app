from cli import runCLI
from todo_list import ToDoList

if __name__ == "__main__":
    todo = ToDoList("tasks.json")
    runCLI(todo)
