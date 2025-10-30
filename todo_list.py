import json
import os
from task import Task

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks_from_file()
        self.next_ID = self.get_next_ID()

    def load_tasks_from_file(self) -> list[Task]:
        """
        Return a list of tasks.

        If a tasks file exists, it will be loaded and the list will be
        populated with existing tasks. Otherwise, a new file will be
        created and an empty list will be returned.

        Returns:
            list[Task]: A list of Task objects representing the current tasks.
        """
        if os.path.exists(self.filename):
            # open existing file
            with open(self.filename, "r") as f:
                data = json.load(f)
            # rebuild list of Task objects from data
            tasks = [Task(**item) for item in data]
        else:
            # file doesn’t exist yet → create one
            with open(self.filename, "w") as f:
                json.dump([], f)
            tasks = []

        return tasks
    
    def list_tasks(self) -> list[str]:
        """
        Return a list of string representations of all tasks.

        Returns:
            list[str]: A list containing string representations of tasks.
            If no tasks exist, the list will contain a single message string.
        """
        if not self.tasks: # empty tasks list
            return ["Your todo list is empty! Please add a task."]
        else:
            return [str(task) for task in self.tasks]
        
    def get_next_ID(self) -> int:
        """
        Return an integer that represents the ID of next available ID

        Returns:
            int: 1 if no tasks exist indicating the start of tasks
            Else the next available ID in tasks
        """
        if not self.tasks:
            return 1 # ID of 1 to start
        else:
            return max(task.id for task in self.tasks) + 1

    def add_task(self, task_description: str) -> None:
        """
        Add a new task to the todo list.

        Args:
            task_description (str): The description of the task to add.
        """
        self.tasks.append(Task(self.next_ID, task_description))