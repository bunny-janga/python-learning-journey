# Day 22: Voice Commands, Speech Recognition and Python Assistant

## 1. Introduction to Voice Commands

Voice commands allow us to control a computer or application using our voice instead of typing.

For example, we can speak commands such as:

- Hello
- What is your name?
- What time is it?
- Open Google
- Exit

Python can recognize spoken words and perform actions based on those words.

### Real-time applications of voice commands

- Voice assistants such as Siri and Google Assistant.
- Smart home devices.
- Voice-controlled applications.
- Hands-free computer operations.
- Accessibility tools for people who have difficulty typing.

### How does a voice command system work?

A basic voice command system follows these steps:

1. The microphone captures our voice.
2. Speech recognition converts the audio into text.
3. Python receives the recognized text.
4. The program checks the command.
5. Python performs the requested action.

### Basic workflow

```text
User speaks
     |
     v
Microphone captures audio
     |
     v
Speech recognition
     |
     v
Text conversion
     |
     v
Python processes the command
     |
     v
Performs an action
```

---

## 2. Speech Recognition Basics

Speech recognition is the process of converting spoken language into written text.

Python provides libraries that help us work with speech recognition.

One popular library is `SpeechRecognition`.

### Installing required libraries

Open your VS Code terminal and run:

```bash
pip install SpeechRecognition
```

For microphone support, install PyAudio:

```bash
pip install pyaudio
```

If PyAudio installation fails on Windows, check the installation instructions for your Python version and operating system. You may need a compatible prebuilt wheel or another supported audio setup.

### Importing the library

```python
import speech_recognition as sr
```

### Important SpeechRecognition components

| Component | Purpose |
|---|---|
| `Recognizer()` | Creates a speech recognition object |
| `Microphone()` | Captures audio from the microphone |
| `listen()` | Records audio |
| `recognize_google()` | Uses Google's speech recognition service to convert audio into text |
| `UnknownValueError` | Handles speech that could not be understood |
| `RequestError` | Handles recognition service or network errors |

### Example: Converting speech into text

```python
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")

    recognizer.adjust_for_ambient_noise(source, duration=1)

    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

except sr.UnknownValueError:
    print("Sorry, I could not understand your voice.")

except sr.RequestError:
    print("Speech recognition service is unavailable.")
```

### Sample output

```text
Speak something...
You said: Hello Python
```

The recognized text depends on what you speak.

### Explanation

**1. Import the library**

We import `speech_recognition` to access its speech recognition features.

**2. Create a recognizer**

```python
recognizer = sr.Recognizer()
```

This object manages the speech recognition process.

**3. Access the microphone**

```python
with sr.Microphone() as source:
```

This opens the microphone so the program can capture audio.

**4. Adjust for background noise**

```python
recognizer.adjust_for_ambient_noise(source, duration=1)
```

This helps the recognizer estimate background noise before listening.

**5. Record audio**

```python
audio = recognizer.listen(source)
```

This captures the user's speech.

**6. Convert speech into text**

```python
text = recognizer.recognize_google(audio)
```

This sends the recorded audio to Google's recognition service and returns the recognized text. An internet connection is required.

**7. Handle errors**

- `UnknownValueError`: The spoken audio could not be understood.
- `RequestError`: The recognition service could not complete the request.

---

## 3. Speech Recognition with Different Commands

We can use conditional statements to perform different actions based on the recognized speech.

### Example

```python
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")

    recognizer.adjust_for_ambient_noise(source, duration=1)

    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()

    print("You said:", command)

    if "hello" in command:
        print("Hello! Welcome to Python.")

    elif "your name" in command:
        print("I am a Python voice assistant.")

    elif "how are you" in command:
        print("I am doing great!")

    else:
        print("Sorry, I don't know that command.")

except sr.UnknownValueError:
    print("Could not understand your speech.")

except sr.RequestError:
    print("Please check your internet connection.")

```

### Sample output

```text
Listening...
You said: hello
Hello! Welcome to Python.
```

### Explanation

- `lower()` converts recognized text into lowercase.
- `if` checks whether the command contains a particular word.
- `elif` checks other possible commands.
- `else` handles commands that are not recognized by our program.

---

## 4. Python Assistant Mini Project

Now let's combine the concepts and build a simple Python voice assistant.

Our assistant will:

1. Greet the user.
2. Listen to voice commands.
3. Tell the current time.
4. Tell today's date.
5. Open Google in a web browser.
6. Respond to simple greetings.
7. Exit when the user says stop or exit.

### Concepts used

- Python functions
- Speech recognition
- Conditional statements
- Loops
- Exception handling
- `datetime` module
- `webbrowser` module

### Complete Python Voice Assistant Program

```python
import speech_recognition as sr
import datetime
import webbrowser


def speak_response(message):
    print("Assistant:", message)


def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source, duration=0.5
        )

        try:
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=5
            )

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return ""

        except sr.RequestError:
            print("Speech recognition service error.")
            return ""

        except OSError:
            print("Microphone is not available.")
            return ""


def process_command(command):

    if "hello" in command:
        speak_response("Hello! How can I help you?")

    elif "your name" in command:
        speak_response("I am your Python voice assistant.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak_response("The current time is " + current_time)

    elif "date" in command:
        today = datetime.date.today().strftime(
            "%d %B %Y"
        )

        speak_response("Today's date is " + today)

    elif "open google" in command:
        speak_response("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "how are you" in command:
        speak_response("I am doing great. Thank you!")

    elif "stop" in command or "exit" in command:
        speak_response("Goodbye! Have a nice day.")
        return False

    else:
        speak_response("Sorry, I don't know that command.")

    return True


def start_assistant():

    speak_response(
        "Welcome! I am your Python voice assistant."
    )

    speak_response(
        "You can ask me the time, date, or open Google."
    )

    while True:

        command = listen_command()

        if command:
            if not process_command(command):
                break


start_assistant()
```

### Sample output

```text
Assistant: Welcome! I am your Python voice assistant.
Assistant: You can ask me the time, date, or open Google.

Listening...
You: Hello
Assistant: Hello! How can I help you?

Listening...
You: What is the time
Assistant: The current time is 02:30 PM

Listening...
You: What is the date
Assistant: Today's date is 01 November 2026

Listening...
You: Open Google
Assistant: Opening Google.

Listening...
You: Exit
Assistant: Goodbye! Have a nice day.
```

The date and time shown above are examples. Your program displays the actual date and time when you run it.

### Explanation of the mini project

**1. Importing modules**

- `speech_recognition` captures and recognizes spoken commands.
- `datetime` provides the current date and time.
- `webbrowser` opens websites in the default browser.

**2. speak_response()**

This function displays the assistant's response in the terminal. It does not produce spoken audio.

**3. listen_command()**

This function activates the microphone, captures audio, and converts speech into text.

**4. process_command()**

This function checks the recognized command and decides which action to perform.

**5. start_assistant()**

This function starts the assistant and keeps listening until the user gives an exit command.

---

## 5. Optional: Making the Assistant Speak

So far, our assistant displays responses as text. We can also make it speak using the `pyttsx3` library.

### Install the library

```bash
pip install pyttsx3
```

### Example

```python
import pyttsx3

engine = pyttsx3.init()

engine.say("Hello! Welcome to Python.")
engine.runAndWait()
```

The computer will speak the sentence aloud using an available system voice.

### Adding speech to the assistant

Replace the earlier `speak_response()` function with:

```python
import pyttsx3

engine = pyttsx3.init()


def speak_response(message):
    print("Assistant:", message)

    engine.say(message)
    engine.runAndWait()
```

Now the assistant can display and speak its responses.

---

## 6. Important Points to Remember

- Speech recognition converts spoken words into text.
- A microphone is required to capture voice input.
- `SpeechRecognition` is a popular Python library for speech recognition.
- `recognize_google()` uses an online recognition service and requires internet access.
- `pyttsx3` can convert text into spoken audio locally using an installed system voice.
- A voice assistant combines multiple Python concepts.
- Background noise can affect speech recognition accuracy.
- Always handle microphone and network errors properly.

## 7. Quick Revision

| Topic | Main purpose |
|---|---|
| Voice Commands | Control applications using spoken instructions |
| Speech Recognition | Convert speech into text |
| `Recognizer()` | Creates a recognition object |
| `Microphone()` | Captures audio |
| `listen()` | Records audio |
| `recognize_google()` | Converts audio into text using an online service |
| `datetime` | Provides date and time |
| `webbrowser` | Opens websites |
| `pyttsx3` | Converts text into speech |

## 8. What I Learned Today

- What voice commands are and how they work.
- How speech recognition converts voice into text.
- How to install and import the SpeechRecognition library.
- How to capture audio through a microphone.
- How to recognize spoken commands.
- How to handle speech recognition errors.
- How to build a simple Python voice assistant.
- How to make the assistant speak using `pyttsx3`.

**Day 22 completed: Voice Commands, Speech Recognition and Python Assistant Mini Project.**
