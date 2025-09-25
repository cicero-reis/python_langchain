from pydantic import BaseModel

class TaskSummaryRequest(BaseModel):
    user_id: int
    task_summary: dict  # total, on_time, late, pending