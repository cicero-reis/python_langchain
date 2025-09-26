from langchain.prompts import PromptTemplate

TASK_SUMMARY_TEMPLATE = """
Usuário {user_name} completou {total} tarefas este mês, sendo {on_time} no prazo, 
{late} atrasadas e {pending} pendentes.
Gere um resumo motivador em 2-3 frases, amigável e claro.
"""
task_summary_prompt_template = PromptTemplate(
    input_variables=["user_name", "total", "on_time", "late", "pending"],
    template=TASK_SUMMARY_TEMPLATE
)
