import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init(driverName='sapi5')

def respond_text_and_voice(text):
    print(f"Aura: {text}")
    speak(text)


def speak(text):
    print("Aura says:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    print("Listening...")
    duration = 5  # seconds
    sample_rate = 16000
    

    try:
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        audio_data = sr.AudioData(audio.tobytes(), sample_rate, 2)

        command = recognizer.recognize_google(audio_data)
        print("You said:", command)
        return command

    except sr.UnknownValueError:
        print("Aura couldn't understand you.")
        speak("Sorry Neo, I didn't catch that.")
        return None

    except sr.RequestError as e:
        print("Speech recognition error:", e)
        speak("There was a problem with my ears.")
        return None

    except Exception as e:
        print("Unexpected error:", e)
        speak("Something went wrong while listening.")
        return None
