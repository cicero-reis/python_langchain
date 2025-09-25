from typing import List, Dict
from .task import Task
from .dto import TaskStatsDTO

class CalculateTaskStatsUseCase:

    def execute(self, tasks: List[Task]) -> Dict[int, TaskStatsDTO]:

        results = {}

        for task in tasks:

            user_id = task.user_id

            if user_id not in results:
                results[user_id] = TaskStatsDTO(0,0,0,0,0.0)

            stats = results[user_id]
            stats.total += 1

            if task.completed_at:
                if task.completed_at <= task.due_date:
                    stats.on_time += 1
                else:
                    stats.late += 1
            else:
                stats.pending += 1

        for user_id, stats in results.items():
            if stats.total > 0:
                stats.percent_on_time = round((stats.on_time / stats.total) * 100, 2)

        return results
