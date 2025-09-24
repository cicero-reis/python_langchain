from src.core.llm.template_query_model import TemplateQueryModel

class GenerateTaskSummaryUserHandler:
    def __init__(self, llm):
        self.llm = llm
        self.query_model = TemplateQueryModel(llm)

    def execute(self, user_id: int, task_summary: dict) -> str:
        return self.query_model.ask_task_summary(user_id, task_summary)
