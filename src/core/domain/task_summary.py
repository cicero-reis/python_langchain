from pydantic import BaseModel

class TaskSummary(BaseModel):
    user_name: str
    task_summary: dict