import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

def summarize_text(text):
    prompt = f"Summarize the following email:\n\n{text}\n\nSummary:"

    response = genai.chat(
        model = genai.GenerativeModel('models/gemini-1.5-pro'),
            messages=[
            {"role": "system", "content": "You are an email summarizer assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

   
        
    
    