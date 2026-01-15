import re
from langchain_core.prompts import PromptTemplate
from .llm import get_llm

PROMPT = PromptTemplate(
    input_variables=["schema", "question"],
    template="""
You are an expert SQLite SQL generator.

Schema:
{schema}

Question:
{question}

Rules:
- SQLite only
- Quote column names with spaces
- Return ONLY SQL
"""
)

def clean_sql(sql: str) -> str:
    sql = sql.strip()
    sql = re.sub(r"```sql|```", "", sql)
    sql = re.sub(r'""+', '"', sql)
    return sql.strip()

def generate_sql(schema, question):
    llm = get_llm()
    raw = llm.invoke(PROMPT.format(schema=schema, question=question)).content
    return clean_sql(raw)
