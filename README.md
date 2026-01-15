AI Text-to-SQL Analyst
Natural Language to SQL using LLMs, FastAPI & SQLite
📌 Problem Statement

Business stakeholders often need insights from structured data but lack SQL knowledge. They rely on analysts or engineers to translate business questions into SQL queries, which leads to:

Delays in decision-making

Increased dependency on technical teams

Inefficient data exploration

Bottlenecks in analytics workflows

Traditional BI tools still require users to understand schemas, joins, and aggregations. This project addresses that gap by enabling natural language querying of structured databases using Large Language Models (LLMs).

🎯 Objective

The goal of this project is to build an AI-powered Text-to-SQL system that allows users to:

Ask business questions in plain English

Automatically generate accurate SQL queries

Execute queries safely on a structured database

Return results in a readable, user-friendly format

All without requiring any SQL knowledge.

🚀 Solution Overview

This application converts natural language questions into executable SQL queries using an LLM-driven agentic pipeline. It combines:

Schema-aware prompt engineering

Controlled SQL generation

Secure query execution

A modern web interface

The system is exposed via a FastAPI backend and a modern frontend UI, making it feel like a real production analytics tool.

🧠 How It Works
1. User Query

The user enters a business question such as:

“Which product has the highest budget?”
“Which state has the highest total sales?”

2. Schema Awareness

The system dynamically reads the database schema, including:

Table names

Column names

Relationships

This schema is injected into the LLM prompt to ensure valid and accurate SQL generation.

3. SQL Generation (LLM)

The LLM:

Understands the intent of the question

Maps it to correct tables and columns

Generates clean, executable SQL only

Avoids hallucinated fields or invalid joins

4. SQL Execution

The generated SQL is executed safely against a SQLite database built from CSV files.

5. Results Rendering

The query result is:

Returned as structured data

Displayed clearly in the UI

Along with the generated SQL for transparency

Architecture
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/e8db0838-00b5-4a36-a442-ebf3914ad326" />



📂 Project Structure
text-to-sql/
│
├── data/
│   ├── 2017_Budgets.csv
│   ├── Customers.csv
│   ├── Products.csv
│   ├── Regions.csv
│   ├── sales_order.csv
│   └── State_Regions.csv
│
├── src/
│   ├── __init__.py
│   ├── agent.py          # Agentic orchestration logic
│   ├── config.py         # Environment & API config
│   ├── database.py       # SQLite DB creation & loading
│   ├── executor.py       # SQL execution layer
│   ├── llm.py            # LLM initialization
│   ├── main.py           # FastAPI application
│   ├── schema.py         # Database schema extraction
│   └── sql_generator.py  # Text-to-SQL logic
│
├── templates/
│   └── index.html        # Modern frontend UI
│
├── static/
│   └── app.js            # Frontend logic
│
├── analytics.db          # SQLite database
├── .env                  # API keys & environment vars
├── .gitignore
└── requirements.txt

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/nishithraj14/text-to-sql.git
cd text-to-sql

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

5️⃣ Run the Application
uvicorn src.main:app --reload


Open in browser:

http://127.0.0.1:8000

🔐 Security & Safety

SQL generation constrained by schema

No raw user SQL execution

Environment variables isolated via .env

Read-only analytical use case

Local database execution

📌 Example Questions

Which product has the highest budget?

Which state has the highest total sales?

Top 5 customers by revenue

Sales distribution by region

Monthly sales trends
