import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTs
from time import ctime

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            aksh_speak(ask)

        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            aksh_speak("Sorry, I did not get that")

        except sr.RequestError:
            aksh_speak("Sorry, My speech service is down")
        return voice_data


def aksh_speak(audio_string):
    tts = gTTs(text=audio_string, lang='en')
    ra = random.randint(1, 10000000)
    audio_file = 'audio-' + str(ra) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio.file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        aksh_speak('My name is Aksh Ridlan')

    if 'what time is it' in voice_data:
        aksh_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        aksh_speak('Here is what I found for' + search)

    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        aksh_speak('Here is the location of' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
aksh_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    aksh_speak(voice_data)
    respond(voice_data)
