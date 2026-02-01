# main.py

from personality import respond
from commands import run_command
from brain import ask_gpt
from voice import speak, listen


from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def main():
    speak("Welcome to Aura. Say something.")
    while True:
        command = listen()
        if not command:
            continue

        try:
            # Send command to GPT-4
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful voice assistant named Aura."},
                    {"role": "user", "content": command}
                ]
            )

            reply = response.choices[0].message.content
            speak(reply)
            print(reply)

            # Optional: run system command and custom logic
            run_command(command)
            ask_gpt(command)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            speak(error_message)
            print(error_message)

if __name__ == "__main__":
    main()
