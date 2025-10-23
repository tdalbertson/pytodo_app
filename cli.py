from todo_list import ToDoList
import shlex

MAIN_COMMANDS = ("add", "update", "delete", "mark-in-progress", "mark-done", "list", "exit")
LIST_ARGUMENTS = ("done", "todo", "in-progress") 
TEXT_COLORS = {
    "PURPLE": "\033[35m",
    "RED": "\033[31m",
    "RESET": "\033[0m",
}


def run_CLI(todo_list: ToDoList) -> None:
    """
    Start an interactive prompt for managing the given to-do list.

    Continuously reads commands (add, update, delete, list, etc.) until the
    user confirms exit.

    Args:
        todo_list: The mutable to-do list instance backing the session.
    """
    running = True

    print(
        f"Welcome to your to-do list app! Please enter a command ({', '.join(command for command in MAIN_COMMANDS)}):"
    )

    while running:
        print(
            f"{TEXT_COLORS['PURPLE']}task-cli {TEXT_COLORS['RESET']}",
            end="",
            flush=True,
        )
        userInput = shlex.split(input())

        match userInput[0].lower():
            case "add":
                if len(userInput) < 2:
                    print("Please enter a task to add")
                else:
                    todo_list.add_task(userInput[1])

            case "update":
                print("You chose 'update'")
            case "delete":
                print("You chose 'delete'")
            case "mark-in-progress":
                print("You chose 'mark-in-progress'")
            case "mark-done":
                print("You chose 'mark-done")
            case "list":
                if len(userInput) < 2:
                    list_command(todo_list)
                elif len(userInput) == 2 and userInput[1] in LIST_ARGUMENTS:
                    pass
                    # check_list_command(userInput[1])
                else:
                    print(f"Please enter a valid list argument: {', '.join(argument for argument in LIST_ARGUMENTS)}")
            case "exit":
                running = confirm_exit()
            case _:
                print(
                    f"{TEXT_COLORS['RED']}Error: Please enter a valid command ({', '.join(command for command in MAIN_COMMANDS)})"
                )

def list_command(todo_list: ToDoList) -> None:
    """
    Print all tasks in the given ToDoList.

    If the todo list is empty, a message will be displayed instead.

    Args:
        todo_list (ToDoList): The ToDoList instance containing tasks to display.
    """
    tasks = todo_list.list_tasks()
    for line in tasks:
        print(line)


def confirm_exit() -> bool:
    """Confirms if the user actually wants to exit this program
    
    Returns:
        Boolean: Represents user's choice to exit or resume.
                - True  -> User chooses to exit
                - False -> User chooses to resume
    """
    confirmation = input("Are you sure you want to exit? (Y/N) ").lower()
    while True:
        if confirmation == "y":
            return False
        elif confirmation == "n":
            return True
        else:
            print(
                f"{TEXT_COLORS['RED']}Please enter a valid value (Y/N){TEXT_COLORS['RESET']} ",
                end="",
                flush=True,
            )
            confirmation = input().lower()

# def check_list_command