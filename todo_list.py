import json
import os
from task import Task

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks_from_file()

    def load_tasks_from_file(self):
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