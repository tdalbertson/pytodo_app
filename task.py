from datetime import datetime
class Task:
    STATUSES = ("todo", "in-progress", "done")

    def __init__(
        self,
        id,
        description,
    ):
        self.id = id
        self.description = description
        self.status = self.STATUSES[0]  # new tasks are automatically 'todo'
        self.createdAt = datetime.now()
        self.updatedAt = (
            self.createdAt  # createdAt & updatedAt are the same when a new task is created
        )

    def __str__(self):
        return f"""
ID: {self.id}
\tDescription: {self.description}
\tStatus: {self.status}
\tCreated At (MM/DD/YYYY): {self.createdAt.strftime("%m/%d/%Y, %H:%M")}
\tUpdated At (MM/DD/YYYY): {self.updatedAt.strftime("%m/%d/%Y, %H:%M")}
"""
