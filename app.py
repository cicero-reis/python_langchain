from fastapi import FastAPI
from langchain_community.llms import Ollama
from src.services.llm_service import LLMService
from src.presentation.routes import get_routes
from src.presentation.routes_generate_task_summary_user_template import get_routes_generate_task_summary_user_template

app = FastAPI()
llm = Ollama(base_url="http://ollama:11434", model="mistral")
llm_service = LLMService(llm)

# Inclui as rotas do arquivo separado
app.include_router(get_routes(llm))
app.include_router(get_routes_generate_task_summary_user_template(llm_service))
