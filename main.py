from task import Task

# CLI-like environment to accept commands

COMMANDS = ("add", "update", "delete")
COLORS = {
    "PURPLE": "\033[35m",
    "RESET": "\033[0m",
}

def runCLI():
    print(
        f"Welcome to your to-do list app! Please enter a command ({', '.join(command for command in COMMANDS)}):"
    )

    while True:
        print(f"{COLORS['PURPLE']}task-cli >{COLORS['RESET']}", end="", flush=True)
        userInput = input().split()
        print(userInput)


if __name__ == "__main__":
    runCLI()
