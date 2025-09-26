from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.llms import Ollama
from src.api.route_task_summary import get_route_task_summary

app = FastAPI()

origins = [
    "http://localhost:5173",  # frontend
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ou ["*"] para permitir todos
    allow_credentials=True,
    allow_methods=["*"],    # GET, POST, PUT, DELETE...
    allow_headers=["*"],    # headers permitidos
)

llm = Ollama(base_url="http://ollama:11434", model="mistral")

app.include_router(get_route_task_summary(llm), prefix="/api")
