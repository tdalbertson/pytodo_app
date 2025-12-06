import shlex
from enum import Enum
from todo_list import ToDoList


class Command(str, Enum):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"
    MARK_TODO = "mark-todo"
    MARK_IN_PROGRESS = "mark-in-progress"
    MARK_DONE = "mark-done"
    LIST = "list"
    EXIT = "exit"


MAIN_COMMANDS = tuple(Command)


class Status(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


STATUSES = tuple(Status)

# Command Indexes
ADD_CMD_STARTING_INDEX = 1
UPDATE_CMD_STARTING_INDEX = 2

# CLI Text Colors
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
    Returns:
        None
    """
    running = True

    print(
        f"Welcome to your to-do list app! Please enter a command ({', '.join(command.value for command in MAIN_COMMANDS)}):"
    )

    while running:
        print(
            f"{TEXT_COLORS['PURPLE']}task-cli {TEXT_COLORS['RESET']}",
            end="",
            flush=True,
        )
        # Command and argument check
        try:
            user_input = shlex.split(input())
            user_input_length = len(user_input)
            try:
                command = Command(user_input[0].lower())
            except ValueError:
                print(
                    f"{TEXT_COLORS['RED']}Error: Please enter a valid command ({', '.join(command.value for command in MAIN_COMMANDS)})"
                )
                continue

            match command:
                case Command.ADD:
                    if not ensure_args_length(
                        user_input_length,
                        2,
                        f"Please enter a task to add\nEx. {Command.ADD.value} Buy groceries",
                    ):
                        continue
                    else:
                        task_description = format_arguments(
                            ADD_CMD_STARTING_INDEX, user_input
                        )
                        todo_list.add_task(task_description)
                case Command.UPDATE:
                    if not ensure_args_length(
                        user_input_length,
                        3,
                        f"Please enter an ID task to {Command.UPDATE.value} and the new task description\nEx. update 1 Buy groceries and cook dinner",
                    ):
                        continue

                    task_id = parse_int(user_input[1])
                    if task_id is None:
                        continue
                    else:
                        new_description = format_arguments(
                            UPDATE_CMD_STARTING_INDEX, user_input
                        )
                        todo_list.update_task(task_id, Command.UPDATE.value, new_description)
                case Command.DELETE:
                    if not ensure_args_length(
                        user_input_length,
                        2,
                        f"Please provide a task ID to {Command.DELETE.value}\nEx. delete 1",
                    ):
                        continue

                    delete_task = confirm_command(user_input[0])
                    task_id = parse_int(user_input[1])
                    if task_id is None:
                        continue

                    if delete_task:
                        todo_list.delete_task(task_id)
                case Command.MARK_TODO:
                    if not ensure_args_length(
                        user_input_length,
                        2,
                        f'Please enter an ID task to change the status to "{Status.TODO.value}".\nEx. mark-todo 1',
                    ):
                        continue

                    task_id = parse_int(user_input[1])
                    mark_todo = Status.TODO.value

                    if task_id is None:
                        continue
                    todo_list.update_task(task_id, Command.MARK_TODO.value, mark_todo)
                case Command.MARK_IN_PROGRESS:
                    if not ensure_args_length(
                        user_input_length,
                        2,
                        f'Please enter an ID task to change the status to "{Status.IN_PROGRESS.value}".\nEx. mark-in-progress 1',
                    ):
                        continue

                    task_id = parse_int(user_input[1])
                    mark_in_progress = Status.IN_PROGRESS.value

                    if task_id is None:
                        continue
                    todo_list.update_task(
                        task_id, Command.MARK_IN_PROGRESS.value, mark_in_progress
                    )
                case Command.MARK_DONE:
                    if not ensure_args_length(
                        user_input_length,
                        2,
                        f'Please enter an ID task to change the status to "{Status.DONE.value}".\nEx. mark-in-progress 1',
                    ):
                        continue

                    task_id = parse_int(user_input[1])
                    mark_done = Status.DONE.value

                    if task_id is None:
                        continue
                    todo_list.update_task(task_id, Command.MARK_DONE.value, mark_done)
                case Command.LIST:
                    if user_input_length < 2:
                        todo_list.list_tasks()
                    elif user_input_length == 2:
                        try:
                            status = Status(user_input[1])
                        except ValueError:
                            print(
                                f"Please enter a valid list status: {', '.join(status.value for status in STATUSES)}"
                            )
                            continue
                        todo_list.list_tasks(status.value)
                    else:
                        print(
                            f"Please enter a valid list status: {', '.join(status.value for status in STATUSES)}"
                        )
                case Command.EXIT:
                    confirm_exit = confirm_command("exit")
                    if confirm_exit:
                        break
                case _:
                    print(
                        f"{TEXT_COLORS['RED']}Error: Please enter a valid command ({', '.join(command.value for command in MAIN_COMMANDS)})"
                    )
        except IndexError:
            print(
                f"{TEXT_COLORS['RED']}Please enter a command.{TEXT_COLORS['RESET']}",
                end="\n",
                flush=True,
            )
            continue


def ensure_args_length(user_args: int, min_args: int, message: str) -> bool:
    """
    Check if the user has provided enough arguments.

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
    """
    Confirms if the user actually wants to execute a command.

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
            return True
        elif confirmation == "N":
            return False
        else:
            print(
                f"{TEXT_COLORS['RED']}Please enter a valid value (Y/N){TEXT_COLORS['RESET']} ",
                end="",
                flush=True,
            )
            confirmation = input().upper()


def format_arguments(starting_index: int, command_arguments: list[str]) -> str:
    """
    Extracts all words after the first (add) and
    concatenates them.

    Args:
        starting_index (int): The index to begin parsing through command_arguments
                Refer to the associated command constants (add, update, etc.)
        command_arguments (list[str]): The arguments the user wants to execute the command on in a
                form that cannot be parsed

    Returns:
        formatted_arguments (str): The arguments formatted for the command
    """
    formatted_arguments = " ".join(command_arguments[starting_index:])

    return formatted_arguments
