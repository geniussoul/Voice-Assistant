Voice Assistant - JARVIS Clone (Python Project)

Overview:
----------
This is a simple Python-based voice assistant that can recognize your speech, respond via text-to-speech, and perform a variety of tasks like telling the time, opening YouTube, playing music, and even cracking jokes. The assistant has been affectionately named "Jarvis" — a tribute to the AI assistant from the Marvel Universe, except this one was created by a genius coder named... you guessed it — Genius.

Features:
----------
- Listens to voice input using microphone
- Recognizes and processes voice commands using Google Speech Recognition
- Replies using text-to-speech engine (pyttsx3)
- Can tell current time
- Opens YouTube in your browser
- Tells a joke using pyjokes
- Plays music from a predefined local directory
- Gracefully exits on command

Technologies Used:
-------------------
- Python
- pyttsx3: For text-to-speech
- speech_recognition: For converting voice to text
- pyjokes: For telling random jokes
- datetime: For fetching current time
- webbrowser: To open web pages
- os: To interact with the system for playing music

How to Run:
-----------
1. Make sure Python is installed on your system.

2. Install required libraries using pip:
   pip install pyttsx3
   pip install SpeechRecognition
   pip install pyjokes
   pip install pyaudio

   Note: If you face errors with pyaudio, you might need to install it from unofficial wheels or use Anaconda.

3. Save the script as "jarvis.py".

4. Run the script:
   python jarvis.py

5. Start speaking commands like:
   - "What is your name?"
   - "How old are you?"
   - "Tell me the time"
   - "Open YouTube"
   - "Tell me a joke"
   - "Play music"
   - "Exit"

Code Description:
------------------
- The function sptext() listens from the microphone and returns the recognized text.
- The function speechtx(x) uses pyttsx3 to convert any string to audible speech.
- The while loop continuously listens for commands and triggers appropriate actions.
- Voice is set to a female voice (voice[1]) and speech rate is slowed for clarity.
- Music is played from the local folder D:/songs (you can change this path).

Commands Recognized:
----------------------
- "your name" : Replies with assistant's name
- "old are you" : Responds with a witty answer about age
- "time" : Tells the current time in 12-hour format
- "youtube" : Opens YouTube in browser
- "joke" : Speaks and prints a random programming joke
- "music" : Plays the last added song from the given folder
- "exit" : Ends the program with a thank-you message

Project Folder Structure:
--------------------------
/Voice-Assistant/
├── jarvis.py        <- Main script file
├── README.txt       <- This file
├── /songs/          <- Folder containing MP3 files for music playback

Possible Future Improvements:
------------------------------
- Add weather forecasting using OpenWeather API
- Integrate ChatGPT API for conversational features
- Implement GUI using Tkinter or PyQt
- Add voice feedback for all tasks (not just print)
- Include speech confirmation for unknown commands
- Add support for calendar or reminder integration

Author Info:
-------------
Name: Martand Mishra (aka Genius)
GitHub: https://github.com/geniussoul
Email: martandmishra473@gmail.com

Fun Quote to Close:
--------------------
"I dream in loops and wake up in try-except blocks. If I had a bug for every thought, I’d be multi-threaded by now." – Genius

License:
---------
This project is open source and free to use for educational purposes.

