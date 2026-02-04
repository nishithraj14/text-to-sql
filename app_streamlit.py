"""
AI Text-to-SQL Analyst – Streamlit Demo

This Streamlit app is a DEMO layer only.
The core system (FastAPI + agentic SQL generation) remains unchanged.

Purpose:
- Showcase Text-to-SQL capability without local setup
- Allow recruiters to explore CSV data
"""

# --------------------------------------------------
# Fix Python path for Streamlit Cloud
# --------------------------------------------------
import sys
import os
sys.path.append(os.getcwd())

# --------------------------------------------------
# Standard imports
# --------------------------------------------------
import pandas as pd
import streamlit as st

from src.agent import agentic_query
from src.database import get_engine
from src.schema import get_schema

# --------------------------------------------------
# Secure OpenAI key handling
# --------------------------------------------------
OPENAI_API_KEY = None
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except Exception:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error(
        "OPENAI_API_KEY not configured.\n\n"
        "• Local: set it in .env\n"
        "• Streamlit Cloud: set it in Secrets"
    )
    st.stop()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="AI Text-to-SQL Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Text-to-SQL Analyst (Demo)")
st.caption(
    "Ask business questions in plain English. "
    "The system generates SQL and executes it on real data."
)

st.divider()

# --------------------------------------------------
# Load database + schema (cached)
# --------------------------------------------------
@st.cache_resource
def load_system():
    engine = get_engine()
    schema = get_schema(engine)
    return engine, schema

engine, schema = load_system()

# --------------------------------------------------
# Sidebar: CSV Browser
# --------------------------------------------------
st.sidebar.header("📁 Available Datasets")

BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")

csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]

selected_csv = st.sidebar.selectbox(
    "Browse CSV files",
    csv_files
)

if selected_csv:
    csv_path = os.path.join(DATA_DIR, selected_csv)
    df = pd.read_csv(csv_path)

    st.sidebar.markdown("**Preview**")
    st.sidebar.dataframe(df.head(10), use_container_width=True)

# --------------------------------------------------
# Reference Questions
# --------------------------------------------------
st.markdown("### 💡 Example Questions")

st.markdown(
    """
- Which state has the highest total sales?
- What are the top 5 products by revenue?
- Show total sales by region.
- Which customers placed the most orders?
- Compare sales across states.
"""
)

st.divider()

# --------------------------------------------------
# Query Interface
# --------------------------------------------------
question = st.text_input(
    "Ask a business question",
    placeholder="Which state has the highest total sales?"
)

if st.button("Run Query") and question:
    with st.spinner("Generating SQL and executing query..."):
        try:
            sql, result_df = agentic_query(schema, engine, question)

            st.subheader("🧠 Generated SQL")
            st.code(sql, language="sql")

            st.subheader("📈 Query Result")
            if isinstance(result_df, pd.DataFrame):
                st.dataframe(result_df, use_container_width=True)
            else:
                st.error(result_df)

        except Exception as e:
            st.error(str(e))

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()
st.caption(
    "Demo UI built with Streamlit. "
    "Core system uses FastAPI, LangChain, and SQLite."
)
