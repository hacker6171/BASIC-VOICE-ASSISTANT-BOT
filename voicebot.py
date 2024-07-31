import speech_recognition as sr
import pyttsx3
import nltk

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def listen():
  with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    try:
      text = recognizer.recognize_google(audio)
      print(f"You said: {text}")
      return text
    except sr.UnknownValueError:
      print("Could not understand audio")
      return None
    except sr.RequestError as e:
      print(f"Could not request results from Google Speech Recognition service; {e}")
      return None

def process_command(command):
  # Basic command handling
  if "hello" in command:
    speak("Hello there!")
  elif "how are you" in command:
    speak("I'm doing well, thank you for asking!")
  else:
    speak("I didn't understand that.")

while True:
  command = listen()
  if command:
    process_command(command)

