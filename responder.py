import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

def suggest_reply(email_body):
    prompt = f"Suggest a polite, professional reply to this email:\n\n{email_body}"

    response = genai.chat(
        model = genai.GenerativeModel('models/gemini-1.5-pro'),
        messages=[
            {"role": "system", "content": "You are an AI assistant that crafts email replies."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

