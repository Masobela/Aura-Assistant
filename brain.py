from openai import OpenAI
from voice import speak
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # ✅ updated model name
            messages=[
                {"role": "system", "content": "You are Aura, a helpful and intelligent assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        speak(answer)
        return answer
    except Exception as e:
        speak("Sorry Neo, I couldn't reach my brain.")
        print("Error:", e)
        return None
