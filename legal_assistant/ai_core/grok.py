import openai
import os
openai.api_key = os.getenv("GEMINI AI")

def get_summary(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or grok equivalent if available via OpenAI-style API
        messages=[
            {"role": "system", "content": "You are a legal assistant."},
            {"role": "user", "content": f"Summarize this legal document:\n{text}"}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

def ask_question(text, question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a legal assistant."},
            {"role": "user", "content": f"Based on this document:\n{text}"},
            {"role": "user", "content": question}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']
