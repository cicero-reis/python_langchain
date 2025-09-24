from langchain.prompts import PromptTemplate

TASK_SUMMARY_TEMPLATE = """
Usuário {user_id} completou {total} tarefas este mês, sendo {on_time} no prazo, 
{late} atrasadas e {pending} pendentes.
Gere um resumo motivador em 2-3 frases, amigável e claro.
"""
prompt_template = PromptTemplate(
    input_variables=["user_id", "total", "on_time", "late", "pending"],
    template=TASK_SUMMARY_TEMPLATE
)
