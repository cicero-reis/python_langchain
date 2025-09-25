from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from src.services.analytics_service import AnalyticsService
from src.core.analytics.task import Task
from src.core.llm.template_query_model import TemplateQueryModel
from src.services.llm_service import LLMService

class TasksRequest(BaseModel):
    tasks: List[Task]

class TaskSummaryRequest(BaseModel):
    user_id: int
    task_summary: dict  # total, on_time, late, pending

analytics_service = AnalyticsService()

def get_routes(llm):

    llm_service = LLMService(llm)

    router = APIRouter()

    @router.post('/analytics')
    def analytics(request: TasksRequest):        
        """
        Retorna o cálculo de tasks por usuário
        """
        return analytics_service.calculate(request.tasks)
    
    @router.post('/generate_task_summary_user_template')
    def generate_task_summary_user_template(request: TaskSummaryRequest):
        """
        Gera um resumo em linguagem natural para o usuário usando LangChain
        """
        return {"summary": llm_service.handle(request.user_id, request.task_summary)}

    return router