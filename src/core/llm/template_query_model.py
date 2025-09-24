from src.core.llm.prompt_template import prompt_template
from json_cache import JSONCache

class TemplateQueryModel:
    def __init__(self, llm):
        self.llm = llm
        self.json_cache = JSONCache()

    def ask_task_summary(self, user_id: int, task_summary: dict) -> str:
        """
        Recebe um task_summary (dicionário) e retorna o texto do LLM,
        usando cache JSON se disponível.
        """
        prompt = prompt_template.format(
            user_id=user_id,
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
