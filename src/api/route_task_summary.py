from fastapi import APIRouter, Depends
from src.core.domain.task_summary import TaskSummary
from src.core.llm.task_summart_llm_service import TaskSummartLLMService

def get_task_summart_llm_service(llm) -> TaskSummartLLMService:
    return TaskSummartLLMService(llm)

def get_route_task_summary(llm):

    router = APIRouter()
    
    @router.post('/tasksummary')
    def feedback(
        request: TaskSummary,
        service: TaskSummartLLMService = Depends(lambda: get_task_summart_llm_service(llm))):
        """
        Generates a natural language summary for the user using LangChain
        """
        return {"summary": service.handle(request.user_name, request.task_summary)}

    return router