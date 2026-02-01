from voice import speak, listen

def respond(command):
    command = command.lower()

    if "hello" in command:
        speak("Hey Neo, ready to change the world?")
        return "handled"

    elif "how are you" in command:
        speak("Feeling electric. What’s on your mind?")
        return "handled"

    elif "exit" in command or "goodbye" in command:
        speak("Are you sure you want to exit? Say yes or no.")
        confirm = listen()
        
        if confirm and "yes" in confirm.lower():
            speak("Goodbye, Neo. Shutting down now.")
            return "force_exit"
        else:
            speak("Alright, staying online.")
            return "handled"

    else:
        return None
    

from memory import remember, recall, forget, recall_all

import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond_text_and_voice(text):
    print(f"Aura: {text}")
    speak(text)


def respond(command):
    command = command.lower()

    if "hello" in command or "hi" in command:
        respond_text_and_voice("Hello Neo, how are you today?")
        return "handled"

    elif "who are you" in command:
        respond_text_and_voice("I am Aura, your AI companion. Half code, half cinematic flair.")
        return "handled"

    elif "tell me a joke" in command:
        respond_text_and_voice("Why do programmers prefer dark mode? Because light attracts bugs.")
        return "handled"

    elif "remember" in command and " is " in command:
        parts = command.split(" is ")
        key = parts[0].replace("remember", "").strip()
        value = parts[1].strip()
        remember(key, value)
        respond_text_and_voice(f"Got it, Neo. I’ll remember your {key} is {value}.")
        return "handled"

    elif "what is my" in command:
        key = command.replace("what is my", "").strip()
        value = recall(key)
        if value:
            respond_text_and_voice(f"Your {key} is {value}, Neo.")
        else:
            respond_text_and_voice(f"I don’t know your {key} yet. Want me to remember it?")
        return "handled"

    elif "forget" in command:
        key = command.replace("forget", "").strip()
        if forget(key):
            respond_text_and_voice(f"I’ve forgotten your {key}, Neo.")
        else:
            respond_text_and_voice(f"I didn’t have your {key} stored.")
        return "handled"

    elif "what do you remember" in command or "list my memories" in command:
        facts = recall_all()
        if facts:
            response = "Here’s what I remember about you, Neo: "
            for key, value in facts.items():
                response += f"Your {key} is {value}. "
            respond_text_and_voice(response)
        else:
            respond_text_and_voice("I don’t have any memories stored yet, Neo.")
        return "handled"

    else:
        return None


 
 
    
