import speech_recognition as sr
import pyaudio
import nltk
import pydub

# # files                                                                         
src = r"./ulatroi.mp3"

dst = r"./ulatroi1.wav"
# dst = r"E:\04-02-2023\folder1\ulatroi.wav"

# convert wav to mp3                                                            
sound = pydub.AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


'''Code nhan dien giong noi'''
r = sr.Recognizer()
with sr.AudioFile(dst) as source:
    audio = r.record(source)
    text = r.recognize_google(audio, language = "vi-VI")
    with open('log.txt', mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
        file.write(str(text))
