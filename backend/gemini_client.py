import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-pro")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def generate_sql_query(question, sql_context):
    prompt = f"""
            You are a helpful assistant that generates SQL queries based on user questions and the provided database schema.

            Schema:
            {sql_context}

            User Question:
            {question}

            SQL Query:
            """
    response = model.generate_content(prompt)
    return response.text.strip()