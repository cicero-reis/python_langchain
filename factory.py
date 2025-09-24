from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain.globals import set_llm_cache
from langchain.cache import SQLiteCache
from json_cache import JSONCache
from src.presentation.routes import get_routes

# Mantém o cache SQLite
set_llm_cache(SQLiteCache(database_path=".langchain.db"))

app = FastAPI()
llm = Ollama(base_url="http://ollama:11434", model="mistral")
json_cache = JSONCache()

# Inclui as rotas do arquivo separado
app.include_router(get_routes(llm, json_cache))