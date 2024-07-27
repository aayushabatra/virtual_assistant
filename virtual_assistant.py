from flask import Flask, request, jsonify
import pyttsx3
import speech_recognition as sr
import datetime
import time
from playsound import playsound

app = Flask(__name__)

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech and speaks it."""
    engine.say(text)
    engine.runAndWait()

def play_music():
    """Plays a predefined music file."""
    try:
        playsound('path_to_music_file.mp3')
        return "Playing your music now."
    except Exception as e:
        return f"Sorry, I couldn't play the music. Error: {e}"

def set_reminder(reminder_time, message):
    """Sets a reminder that alerts after a specified time."""
    speak(f"Reminder set for {reminder_time}.")
    time.sleep(reminder_time * 60)
    speak(message)
    return "Reminder completed."

@app.route('/')
def home():
    return "Welcome to Caspher Virtual Assistant API!"

@app.route('/play_music', methods=['GET'])
def handle_play_music():
    result = play_music()
    return jsonify({"message": result})

@app.route('/set_reminder', methods=['POST'])
def handle_set_reminder():
    data = request.json
    reminder_time = data.get('time', 0)
    message = data.get('message', 'No message provided.')
    result = set_reminder(reminder_time, message)
    return jsonify({"message": result})

@app.route('/speak', methods=['POST'])
def handle_speak():
    data = request.json
    text = data.get('text', 'No text provided.')
    speak(text)
    return jsonify({"message": "Speaking done."})

if __name__ == "__main__":
    app.run(debug=True)
