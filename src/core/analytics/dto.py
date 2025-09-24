from dataclasses import dataclass

@dataclass
class TaskStatsDTO:
    total: int
    on_time: int
    late: int
    pending: int
    percent_on_time: float