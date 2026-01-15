from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from src.agent import agentic_query
from src.database import get_engine
from src.schema import get_schema

app = FastAPI(title="AI Text-to-SQL Analyst")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

engine = get_engine()
schema = get_schema(engine)

class QueryRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/query")
def query_sql(data: QueryRequest):
    sql, df = agentic_query(schema, engine, data.question)
    return {
        "sql": sql,
        "result": df.to_dict(orient="records")
    }
