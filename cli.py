from task import Task
import shlex
import os
import json

COMMANDS = ("add", "update", "delete", "mark-in-progress", "mark-done", "list", "exit")
TEXT_COLORS = {
    "PURPLE": "\033[35m",
    "RED": "\033[31m",
    "RESET": "\033[0m",
}


def runCLI():
    """Begins CLI-like environment to accept todo commands"""
    running = True

    print(
        f"Welcome to your to-do list app! Please enter a command ({', '.join(command for command in COMMANDS)}):"
    )

    while running:
        print(
            f"{TEXT_COLORS['PURPLE']}task-cli > {TEXT_COLORS['RESET']}",
            end="",
            flush=True,
        )
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
            case "mark-in-progress":
                print("You chose 'mark-in-progress'")
            case "mark-done":
                print("You chose 'mark-done")
            case "list":
                print("You chose 'list'")
            case "exit":
                running = confirmExit()
            case _:
                print(
                    f"{TEXT_COLORS['RED']}Error: Please enter a valid command ({', '.join(command for command in COMMANDS)})"
                )


def confirmExit() -> bool:
    """Confirms if the user actually wants to exit this program"""
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
