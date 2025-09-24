from src.core.analytics.task import Task
from src.core.analytics.calculate_task_stats_use_case import CalculateTaskStatsUseCase
from datetime import datetime

class AnalyticsService:
    def __init__(self):
        self.use_case = CalculateTaskStatsUseCase()

    def calculate(self, tasks):
        # tasks é uma lista de Task
        user_stats = {}
        for task in tasks:
            user_id = task.user_id
            if user_id not in user_stats:
                user_stats[user_id] = {"total": 0, "on_time": 0, "late": 0, "pending": 0}
            
            user_stats[user_id]["total"] += 1
            if task.completed_at is None:
                user_stats[user_id]["pending"] += 1
            elif task.completed_at <= task.due_date:
                user_stats[user_id]["on_time"] += 1
            else:
                user_stats[user_id]["late"] += 1

        return user_stats

# from datetime import datetime

# def calculate_task_stats(tasks):
#     results = {}

#     for task in tasks:
#         user_id = task["user_id"]
#         due_date = datetime.fromisoformat(task["due_date"])
#         completed_at = task.get("completed_at")

#         if user_id not in results:
#             results[user_id] = {
#                 "total": 0,
#                 "on_time": 0,
#                 "late": 0,
#                 "pending": 0,
#                 "percent_on_time": 0.0
#             }

#         results[user_id]["total"] += 1

#         if completed_at:
#             completed_dt = datetime.fromisoformat(completed_at)
#             if completed_dt <= due_date:
#                 results[user_id]["on_time"] += 1
#             else:
#                 results[user_id]["late"] += 1
#         else:
#             results[user_id]["pending"] += 1

#     # calcular percentuais
#     for user_id, stats in results.items():
#         if stats["total"] > 0:
#             stats["percent_on_time"] = round((stats["on_time"] / stats["total"]) * 100, 2)

#     return results
