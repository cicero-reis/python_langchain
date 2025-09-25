from src.core.llm.generate_task_summary_user_handler import GenerateTaskSummaryUserHandler
from src.core.llm.llm_service_abstract import LLMServiceAbstract

class LLMService(LLMServiceAbstract):
    def __init__(self, llm):
        self.use_case: GenerateTaskSummaryUserHandler = GenerateTaskSummaryUserHandler(llm)

    def handle(self, user_id: int, task_summary: dict) -> str:
        return self.use_case.execute(user_id, task_summary)
