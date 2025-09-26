from abc import ABC, abstractmethod

class TaskSummaryLLMServiceAbstract(ABC):
    @abstractmethod
    def handle(self, user_id: int, task_summary: dict) -> str:
        pass