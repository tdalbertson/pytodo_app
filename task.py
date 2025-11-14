from datetime import datetime
class Task:
    STATUSES = ("todo", "in-progress", "done")

    def __init__(
        self,
        id,
        description,
        status=None,
        created_at=None,
        updated_at=None
    ):
        self.id = id
        self.description = description
        self.status = self.STATUSES[0]  # new tasks are automatically 'todo'
        self.created_at = datetime.now()
        self.updated_at = (
            self.created_at  # created_at & updated_at are the same when a new task is created
        )

    def __str__(self):
        return f"""
ID: {self.id}
\tDescription: {self.description}
\tStatus: {self.status}
\tCreated At (MM/DD/YYYY): {self.created_at.strftime("%m/%d/%Y, %H:%M")}
\tUpdated At (MM/DD/YYYY): {self.updated_at.strftime("%m/%d/%Y, %H:%M")}
"""
    
    def to_dict(self) -> dict:
        """
        Converts a Task object into a dictionary format for JSON serialization

        Args:
            None
        
        Returns:
            dict: A dictionary representation of the Task with all attributes
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
