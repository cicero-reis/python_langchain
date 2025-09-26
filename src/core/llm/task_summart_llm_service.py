from src.core.llm.task_summary_handler import TaskSummaryHandler
from src.core.llm.task_summary_llm_service_abstract import TaskSummaryLLMServiceAbstract

class TaskSummartLLMService(TaskSummaryLLMServiceAbstract):
    def __init__(self, llm):
        self.use_case: TaskSummaryHandler = TaskSummaryHandler(llm)

    def handle(self, user_id: int, task_summary: dict) -> str:
        return self.use_case.execute(user_id, task_summary)
