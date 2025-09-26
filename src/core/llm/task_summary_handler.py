from src.template.task_summary_template_query_model import TaskSummaryTemplateQueryModel

class TaskSummaryHandler:
    def __init__(self, llm):
        self.llm = llm
        self.query_model = TaskSummaryTemplateQueryModel(llm)

    def execute(self, user_id: int, task_summary: dict) -> str:
        return self.query_model.ask_task_summary(user_id, task_summary)
