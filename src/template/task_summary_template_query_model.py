from src.prompt.task_summary_prompt import task_summary_prompt_template
from json_cache import JSONCache

class TaskSummaryTemplateQueryModel:
    def __init__(self, llm):
        self.llm = llm
        self.json_cache = JSONCache()

    def ask_task_summary(self, user_name: str, task_summary: dict) -> str:
        """
        Receives a task_summary (dictionary) and returns the LLM text,
        using JSON cache if available.
        """
        prompt = task_summary_prompt_template.format(
            user_name=user_name,
            total=task_summary["total"],
            on_time=task_summary["on_time"],
            late=task_summary["late"],
            pending=task_summary["pending"]
        )

        # Identificador único do LLM
        lm_string = f"{self.llm.model}:{self.llm.base_url}"

        cached = self.json_cache.lookup(prompt, lm_string)
        if cached is not None:
            return cached

        response = self.llm.invoke(prompt)
        self.json_cache.update(prompt, lm_string, response)
        return response
