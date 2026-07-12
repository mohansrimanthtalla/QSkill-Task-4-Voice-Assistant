import pyttsx3
import webbrowser
import os
import subprocess
from datetime import datetime

# ==========================
# Text to Speech Function
# ==========================
def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)

    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ==========================
# Start Assistant
# ==========================
print("=" * 50)
print("        Voice Assistant Started")
print("=" * 50)

speak("Hello Mohan! Welcome to your Voice Assistant.")

# ==========================
# Main Loop
# ==========================
while True:

    command = input("\nYou: ").strip().lower()

    # --------------------------
    # Greetings
    # --------------------------
    if command == "hello":
        speak("Hello Mohan! How are you?")

    # --------------------------
    # Time
    # --------------------------
    elif command == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # --------------------------
    # Date
    # --------------------------
    elif command == "date":
        today = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    # --------------------------
    # Open Websites
    # --------------------------
    elif command == "open google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command == "open youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command == "open github":
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # --------------------------
    # Open Applications
    # --------------------------
    elif command == "open notepad":
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")

    elif command == "open calculator":
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")

    elif command == "open cmd":
        speak("Opening Command Prompt")
        subprocess.Popen("cmd.exe")

    elif command == "open paint":
        speak("Opening Paint")
        subprocess.Popen("mspaint.exe")

    elif command == "open explorer":
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")

    # --------------------------
    # Reminders
    # --------------------------
    elif command == "add reminder":

        reminder = input("Enter reminder: ")

        with open("reminders.txt", "a") as file:
            file.write(reminder + "\n")

        speak("Reminder saved successfully.")

    elif command == "show reminders":

        if os.path.exists("reminders.txt"):

            with open("reminders.txt", "r") as file:
                reminders = file.readlines()

            if len(reminders) == 0:
                speak("No reminders found.")

            else:
                speak("Here are your reminders.")

                for i, reminder in enumerate(reminders, start=1):
                    print(f"{i}. {reminder.strip()}")

        else:
            speak("No reminders file found.")

    # --------------------------
    # Calculator
    # --------------------------
    elif command == "calculator":

        try:
            num1 = float(input("First Number: "))
            operator = input("Operator (+ - * /): ")
            num2 = float(input("Second Number: "))

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    speak("Division by zero is not allowed.")
                    continue
                result = num1 / num2

            else:
                speak("Invalid operator.")
                continue

            print("Result =", result)
            speak(f"The answer is {result}")

        except ValueError:
            speak("Invalid input.")

    # --------------------------
    # Help Menu
    # --------------------------
    elif command == "help":

        print("\n========== AVAILABLE COMMANDS ==========")
        print("hello")
        print("time")
        print("date")
        print("open google")
        print("open youtube")
        print("open github")
        print("open notepad")
        print("open calculator")
        print("open cmd")
        print("open paint")
        print("open explorer")
        print("add reminder")
        print("show reminders")
        print("calculator")
        print("help")
        print("bye")
        print("========================================")

        speak("These are the available commands.")

    # --------------------------
    # Exit
    # --------------------------
    elif command == "bye":
        speak("Goodbye Mohan! Have a wonderful day.")
        break

    # --------------------------
    # Unknown Command
    # --------------------------
    else:
        speak("Sorry, I don't understand that command.")