from fastapi import FastAPI
from langchain_community.llms import Ollama
from src.api.route_task_summary import get_route_task_summary

app = FastAPI()

llm = Ollama(base_url="http://ollama:11434", model="mistral")

app.include_router(get_route_task_summary(llm), prefix="/api")
