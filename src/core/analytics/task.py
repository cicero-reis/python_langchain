from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    user_id: int
    due_date: datetime
    completed_at: Optional[datetime] = None