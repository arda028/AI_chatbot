import os
from flask import Flask, request, jsonify, render_template
from gemini_client import generate_sql_query

# Define base directory relative to app.py
base_directory = os.path.abspath(os.path.dirname(__file__))

# Initialize Flask app with correct paths to frontend files
app = Flask(
    __name__,
    template_folder=os.path.join(base_directory, '/Users/ardatongo/Desktop/chatbot/frontend/templates'),
    static_folder=os.path.join(base_directory, '/Users/ardatongo/Desktop/chatbot/frontend/static')
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    sql_context = request.args.get('context', '')
    return render_template('chat.html', sql_query=sql_context)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get("question")
    sql_context = data.get("sql_query", "")
    response = generate_sql_query(user_input, sql_context)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)