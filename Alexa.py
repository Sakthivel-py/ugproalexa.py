import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import time
import random
import os
import requests
import webbrowser
import wikipedia
import pywhatkit


# Make Alexa To Speak
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    print(audio)


# To Open Vlc Media Player
def media():
    speak("Opening Vlc media Player")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN\\VLC media player"
    os.startfile(path)


# TO Close Vlc Media Player
def close_media():
    speak("Closing Vlc media player")
    os.system("task kill /f /im medial.exe")


# To Open Command Prompt
def cmd():
    speak("Opening Command Prompt...")
    os.system("start cmd")


# To Play Music
def music():
    speak("Playing Music....")
    music_dir = "D:\\MUSIC"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir, rd))


# To Open YouTube
def Youtube():
    speak("Opening Youtube...")
    webbrowser.open("www.youtube.com")


# To Open Facebook
def FaceBook():
    speak("Opening FaceBook....")
    webbrowser.open("www.facebook.com")


# To Search On Google
def google():
    speak("What Should I Search On Google, Sir....")
    qn = take_command().lower()
    webbrowser.open(qn)


# To Search On Wikipedia
def wiki():
    speak("What You Want Search On Wikipedia....")
    qn = take_command()
    result = wikipedia.summary(qn, sentences=2)
    speak(f"According To Wikipedia{result}")
    print(result)


# To Play YouTube Content
def play_yt():
    speak("What Video Do You Want On YouTube... ")
    name = take_command()
    speak("Playing  " + name)
    pywhatkit.playonyt(name)


# To Send Whatsapp Message
def what_msg():
    speak("Enter The Whatsapp Mobile Number...")
    no = input("Enter The Whatsapp Mobile Number:")
    speak("Tell Me The Message...")
    msg = take_command()
    speak("Please Specify The Time...")
    hour = int(input("Enter The Hour : "))
    minu = int(input("Enter The Minutes : "))
    pywhatkit.sendwhatmsg(no, msg, hour, minu)


# To Close Command Prompt
def close_cmd():
    speak("Closing Command Prompt")
    os.system("task kill /f /im cmd.exe")


# To Take Command From User
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said :{query}")

    except:
        speak("Say That Again Please")

    return query


# To Find IP Address Of The System
def ip_address():
    ip = requests.get("https://api.ipify.org").text
    speak(f"Your IP Address is {ip}")


# To Make Alexa To Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I %M %p")

    if 0 <= hour <= 12:
        a = "Good Morning Sir.... ", "Hello sir..."
        speak(random.choice(a) + "It Is" + tt)
    elif 12 <= hour < 16:
        a = "Good Afternoon Sir....", "Hello sir..."
        speak(random.choice(a) + "It Is" + tt)
    elif 16 < hour <= 19:
        a = "Good Evening Sir.... ", "Hello Sir...... "
        speak(random.choice(a) + "It Is" + tt)
    else:
        a = "Good Night Sir.... ", "Hello Sir...... "
        speak(random.choice(a) + "It Is" + tt)

    b = "How May I Help You Sir...", "Give Me A Command Sir....", "Online And Ready Sir..."
    speak("I Am Alexa " + random.choice(b))


if __name__ == '__main__':
    wish()

    query = take_command()
    if "open VLC media player" in query:
        media()
    elif "open CMD" in query:
        cmd()

    elif "close Vlc media player" in query:
        close_media()

    elif "close CMD" in query:
        close_cmd()

    elif "IP address" in query:
        ip_address()

    elif "play music" in query:
        music()

    elif "open YouTube" in query:
        Youtube()

    elif "open Facebook" in query:
        FaceBook()

    elif "open Google" in query:
        google()

    elif "search on Wikipedia" in query:
        wiki()

    elif "play on YouTube" in query:
        play_yt()

    elif "send message on WhatsApp" in query:
        what_msg()

