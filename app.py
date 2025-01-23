import sounddevice as sd
import numpy as np
import speech_recognition as sr
from ollama import chat
from ollama import ChatResponse
from gtts import gTTS
from pygame import mixer
import os
import time

#--------------------------------------------------------------
#
#
#
#--------------------------------------------------------------

mixer.init()

def transcribe(frequence=44100):
    audio = []

    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio.append(indata.copy())

    # Enregistrer l'audio avec SoundDevice
    input("Press [ENTER] to START recording...\n")
    with sd.InputStream(samplerate=frequence, channels=1, callback=callback, dtype='float32'):
        input("Press [ENTER] to STOP recording...\n")
        print("Saving audio...")

    # Convertir les blocs en un tableau NumPy
    audio = np.concatenate(audio, axis=0)

    # Convertir les données float32 en int16 pour SpeechRecognition
    audio_int16 = np.int16(audio * 32767)

    # Transcrire l'audio avec SpeechRecognition
    recognizer = sr.Recognizer()
    try:
        print("Processing audio...")
        # Créer un objet AudioData compatible avec SpeechRecognition
        audio_data = sr.AudioData(audio_int16.tobytes(), frequence, 2)
        text = recognizer.recognize_google(audio_data, language="fr-FR")  # Langue française
        print("💬 You say:")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Unable to recognize your voice...")
        return None
    except sr.RequestError as e:
        print(f"Internal error : {e}")
        return None
    
def say(phrase):
    tts = gTTS(phrase, lang='fr')

    filename = 'output.mp3'

    tts.save(filename)

    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    os.remove(filename)    

print("👋 Welcome to Talk2Me 0.1")

say("Bonjour, je suis une intelligence artificielle à votre service")

while True:
    say("Comment puis-je vous aider?")

    # Exemple d'utilisation
    extraction = transcribe()

    if extraction is not None:
        say("Je réfléchis...")

        # llama3.2:1b
        # llama3.2:3b
        # gemma:3b
        # mistral
        response: ChatResponse = chat(model='llama3.2:3b', messages=[
        {
            'role': 'user',
            'content': 'Répond de manière brève en français à cette question: ' + extraction,
        },
        ])

        answer = response.message.content
        print("🤖 AI says:")
        print(answer)
        
        answer = answer.replace("*", " ")
        say(answer)
