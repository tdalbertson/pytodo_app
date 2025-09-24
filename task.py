class Task:
    def __init__(self):
        self.description = self.getDescription()
        self.completed = self.getCompleted()

    def getDescription(self) -> str:
        task_desc = ""

        while not task_desc.strip():
            task_desc = input("What is the task? ")
            if not task_desc:
                print("Error: Task cannot be empty. Try again.")

        return task_desc

    def getCompleted(self) -> str:
        completion_status = ""

        while not completion_status.strip():
            completion_status = input("Has this task been completed? ")
            if not completion_status:
                print("Error: Completion status cannot be empty. Try again.")

        return completion_status

    def __str__(self):
        return f"Task: {self.description}\nCompletion status: {self.completed}"
