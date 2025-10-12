from task import Task
import shlex

# CLI-like environment to accept commands

COMMANDS = ("add", "update", "delete")
TEXT_COLORS = {
    "PURPLE": "\033[35m",
    "RED": "\033[31m",
    "RESET": "\033[0m",
}

def runCLI():
    print(
        f"Welcome to your to-do list app! Please enter a command ({', '.join(command for command in COMMANDS)}):"
    )

    while True:
        print(f"{TEXT_COLORS['PURPLE']}task-cli > {TEXT_COLORS['RESET']}", end="", flush=True)
        userInput = shlex.split(input())

        match userInput[0].lower():
            case "add":
                if len(userInput) < 2:
                    print("Please enter a task to add")
                else:
                    print(f'You added "{userInput[1]}"')
            case "update":
                print("You chose 'update'")
            case "delete":
                print("You chose 'delete'")
            case _:
                print(
                    f"{TEXT_COLORS['RED']}Error: Please enter a valid command ({', '.join(command for command in COMMANDS)})"
                )
