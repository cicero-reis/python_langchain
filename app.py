from fastapi import FastAPI
from langchain_community.llms import Ollama
from src.presentation.routes import get_routes

app = FastAPI()
llm = Ollama(base_url="http://ollama:11434", model="mistral")

# Inclui as rotas do arquivo separado
app.include_router(get_routes(llm))
