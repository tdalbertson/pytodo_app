from todo_list import ToDoList
import shlex

MAIN_COMMANDS = (
    "add",
    "update",
    "delete",
    "mark-in-progress",
    "mark-done",
    "list",
    "exit",
)
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
        user_input = shlex.split(input())
        user_input_length = len(user_input)

        # Command and argument check
        match user_input[0].lower():
            case "add":
                if not ensure_args_length(
                    user_input_length,
                    2,
                    'Please enter a task to add\nEx. add "Buy groceries"',
                ):
                    continue
                else:
                    todo_list.add_task(user_input[1])
            case "update":
                if not ensure_args_length(
                    user_input_length,
                    3,
                    'Please enter an ID task to update and the new task text\nEx. update 1 "Buy groceries and cook dinner"',
                ):
                    continue
                
                task_id = parse_int(user_input[1])
                if task_id is None:
                    continue

                print("You chose 'update'")
            case "delete":
                if not ensure_args_length(
                    user_input_length,
                    2,
                    "Please provide a task ID to delete\nEx. delete 1",
                ):
                    continue
                
                task_id = parse_int(user_input[1])
                if task_id is None:
                    continue

                todo_list.remove_task(task_id)
            case "mark-in-progress":
                print("You chose 'mark-in-progress'")
            case "mark-done":
                print("You chose 'mark-done")
            case "list":
                if user_input_length < 2:
                    list_command(todo_list)
                elif user_input_length == 2 and user_input[1] in LIST_ARGUMENTS:
                    pass
                    # check_list_command(user_input[1])
                else:
                    print(
                        f"Please enter a valid list argument: {', '.join(argument for argument in LIST_ARGUMENTS)}"
                    )
            case "exit":
                running = confirm_command("exit")
            case _:
                print(
                    f"{TEXT_COLORS['RED']}Error: Please enter a valid command ({', '.join(command for command in MAIN_COMMANDS)})"
                )


def ensure_args_length(user_args: int, min_args: int, message: str) -> bool:
    """Check if the user has provided enough arguments.

    Args:
        user_args (int): The number of user-provided arguments
        min_args (int): The minimum number of arguments for a given command
        message (str): The error message to display if a user inputs too few arguments

    Returns:
        Boolean:
            True: User provided enough arguments
            False: User did not provide enough arguments
    """
    if user_args < min_args:
        print(message)
        return False
    return True


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


def parse_int(
    value: str, error_message: str = "Please enter a valid number."
) -> int | None:
    """Attempt to convert a user-provided value into an integer.

    Args:
        value (str): The raw user input to convert
        error_message (str): The message to display if conversion fails

    Returns:
        int | None:
            int: The successfully converted integer value
            None: The input could not be converted to an integer
    """
    try:
        return int(value)
    except ValueError:
        print(error_message)
        return None


def confirm_command(command: str) -> bool:
    """Confirms if the user actually wants to execute a command.

    Args:
        command (str): The user command to confirm

    Returns:
        Boolean: Represents user's choice to execute command.
                True: User chooses to execute command.
                False: User chooses not to execute command.
    """
    confirmation = input(f"Are you sure you want to {command}? (Y/N) ").upper()
    while True:
        if confirmation == "Y":
            return False
        elif confirmation == "N":
            return True
        else:
            print(
                f"{TEXT_COLORS['RED']}Please enter a valid value (Y/N){TEXT_COLORS['RESET']} ",
                end="",
                flush=True,
            )
            confirmation = input().upper()
