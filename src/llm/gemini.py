import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(api_key[:10])
print("API Key Loaded:", bool(api_key))

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

async def extract_json(text: str):
    print("Sending request to Gemini...")

    prompt = f"""
Extract structured information as JSON.

{text}
"""

    try:
        response = model.generate_content(prompt)
        print("Received response from Gemini")
        return response.text

    except Exception as e:
        print("Gemini Error:", repr(e))
        return None