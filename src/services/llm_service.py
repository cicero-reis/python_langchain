from src.core.llm.generate_task_summary_user_handler import GenerateTaskSummaryUserHandler

class LLMService:
    def __init__(self, llm):
        self.use_case = GenerateTaskSummaryUserHandler(llm)

    def generate_summary(self, user_id: int, task_summary: dict) -> str:
        return self.use_case.execute(user_id, task_summary)
