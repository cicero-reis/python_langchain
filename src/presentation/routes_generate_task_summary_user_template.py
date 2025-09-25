from fastapi import Depends
from src.presentation.request.task_summary_request import TaskSummaryRequest
from src.presentation.router import get_router
from src.core.llm.llm_service_abstract import LLMServiceAbstract


def get_routes_generate_task_summary_user_template(llm_service: LLMServiceAbstract):

    router = get_router()
    
    @router.post('/generate_task_summary_user_template')
    def generate_task_summary_user_template(
        request: TaskSummaryRequest,
        service: LLMServiceAbstract = Depends(lambda: llm_service)):
        """
        Gera um resumo em linguagem natural para o usuário usando LangChain
        """
        return {"summary": service.handle(request.user_id, request.task_summary)}

    return router