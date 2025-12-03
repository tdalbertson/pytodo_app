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
        # If status/timestamps were provided (e.g., when loading from existing tasks file), keep them.
        self.status = status or self.STATUSES[0]
        self.created_at = (
            datetime.fromisoformat(created_at)
            if created_at
            else datetime.now()
        )
        self.updated_at = (
            datetime.fromisoformat(updated_at)
            if updated_at
            else self.created_at
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
