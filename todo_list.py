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
        populated with existing tasks. 
        Otherwise, a new file will be created and an empty list will be returned.

        Returns:
            list[Task]: A list of Task objects representing the current tasks.
        """
        if os.path.exists(self.filename):
            # Open existing file
            with open(self.filename, "r") as f:
                data = json.load(f)
            # Rebuild list of Task objects from data
            return [
                Task(
                    id=item["id"],
                    description=item["description"],
                    status=item["status"],
                    created_at=item["created_at"],
                    updated_at=item["updated_at"],
                )
                for item in data
            ]
        else:
            # File doesn’t exist yet → Create empty file
            tasks = []
            with open(self.filename, "w") as f:
                json.dump(tasks, f, indent=4)
            return tasks

    def write_tasks_to_file(self) -> None:
        """
        Overwrite related tasks JSON file with data from CLI

        Args:
            None
        Returns:
            None
        """
        with open(self.filename, "w") as f:
            tasks_data = [task.to_dict() for task in self.tasks]

            json.dump(tasks_data, f, indent=4)

    #TODO
    def list_tasks(self, status=None) -> list[str]:
        """
        Return a list of string representations of tasks.
        If a status is provided, tasks with associated status will be returned.
        Otherwise, all tasks in the list will be returned.

        Returns:
            list[str]: A list containing string representations of tasks.
            If no tasks exist, the list will contain a single message string.
        """
        if not self.tasks:  # empty tasks list
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
            return 1  # ID of 1 to start
        else:
            return max(task.id for task in self.tasks) + 1

    def add_task(self, task_description: str) -> None:
        """
        Add a new task to the todo list.

        Args:
            task_description (str): The description of the task to add.
        Returns:
            None
        """
        self.tasks.append(Task(self.next_ID, task_description))

    def remove_task(self, id: int) -> None:
        """
        Removes a task from the todo list.
        If an ID cannot be found, the user is shown an failure message.
        Otherwise, the associated task is removed from the list and the user is shown a success message.

        Args:
            id (int): The id of the task to remove.
        Returns:
            None
        """
        task_index = self.get_task_by_id(id)
        if task_index is None:
            print(
                f"Task with ID {id} could not be found. Please try again with another ID."
            )
        else:
            removed_task = self.tasks.pop(task_index)
            print(f"Removed task: {removed_task.description}")

    def get_task_by_id(self, target_id: int) -> int | None:
        """
        Helper method for locating the index of a task in the tasks list.

        Args:
            target_id (int): The ID of the task to locate.

        Returns:
            int: If found, returns the index of the task within the tasks list
            None: Else, the target tasks does not exist within the tasks list
        """
        for i, task in enumerate(self.tasks):
            if task.id == target_id:
                return i
        return None

    def update_task_status(self, id: int, status: str) -> None:
        """
        Update a task's status based on specified status.
        If an ID cannot be found, the user is shown an failure message.
        Otherwise, the associated task's status is updated and the user is shown a success message.

        Args:
        task_id (int): The ID of a task to update.
        status (str): The new task status to set.

        Returns:
            None
        """
        task_index = self.get_task_by_id(id)
        if task_index is None:
            print(
                f"Task with ID {id} could not be found. Please try again with another ID."
            )
        else:
            updated_task = self.tasks[task_index]
            updated_task.status = status
            print(f"Updated task {updated_task.description} to {status}")