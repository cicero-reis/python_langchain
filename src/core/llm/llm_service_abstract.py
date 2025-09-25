from abc import ABC, abstractmethod

class LLMServiceAbstract(ABC):
    @abstractmethod
    def handle(self, user_id: int, task_summary: dict) -> str:
        pass