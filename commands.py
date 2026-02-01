import os
import webbrowser
from voice import speak
from voice import listen, speak
import config



def run_command(command):
    command = command.lower()

    if "open chrome" in command:
        speak("Opening Google Chrome...")
        os.system("start chrome")

    elif "open youtube" in command:
        speak("Launching YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "open notepad" in command:
        speak("Opening Notepad...")
        os.system("notepad")

    elif "play music" in command:
        speak("Playing your music...")
        # Adjust path to your music folder or file
        os.system("start wmplayer C:\\Users\\amaso\\Music")

    else:
        speak("Sorry Neo, I don’t know that command yet.")
        import os
import sys

def run_command(command):
    if "shutdown" in command or "turn off laptop" in command:
        speak("Shutting down your laptop now.")
        os.system("shutdown /s /t 1")  # Windows shutdown
        return "handled"

    elif "restart" in command or "reboot laptop" in command:
        speak("Rebooting your laptop now.")
        os.system("shutdown /r /t 1")  # Windows restart
        return "handled"

    # Add more commands here...elif "shutdown" in command:
    speak("Are you sure you want to shut down your laptop? Say yes or no.")
    confirm = listen()
    if confirm and "yes" in confirm.lower():
        speak("Goodbye, Neo. Powering down now.")
        os.system("shutdown /s /t 1")
        return "force_exit"
    else:
        speak("Alright, staying online.")
        return "handled"

import os
from voice import listen, speak

def run_command(command):
    if "shutdown" in command or "turn off laptop" in command:
        speak("Are you sure you want to shut down your laptop? Say yes or no.")
        confirm = listen()
        if confirm and "yes" in confirm.lower():
            speak("Goodbye, Neo. Powering down now.")
            os.system("shutdown /s /t 1")  # Windows shutdown
            return "force_exit"
        else:
            speak("Alright, staying online.")
            return "handled"

    elif "restart" in command or "reboot laptop" in command:
        speak("Are you sure you want to restart your laptop? Say yes or no.")
        confirm = listen()
        if confirm and "yes" in confirm.lower():
            speak("Rebooting your laptop now.")
            os.system("shutdown /r /t 1")  # Windows restart
            return "force_exit"
        else:
            speak("Restart cancelled.")
            return "handled"

    elif "sleep" in command or "go to sleep" in command:
        speak("Putting your laptop to sleep. Wake me up when you’re ready.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Windows sleep
        return "force_exit"

    elif "sleep aura" in command or "sleep mode" in command:
        speak("Aura is going quiet. Say 'wake up' when you need me.")
        while True:
            wake = listen()
            if wake and "wake up" in wake.lower():
                speak("Aura is back online.")
                return "handled"

    else:
        return None



