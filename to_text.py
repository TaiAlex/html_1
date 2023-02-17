import glob
import os.path
import pydub
import speech_recognition as sr
import pyaudio

def mp3_to_wav():
    folder_path = r'E:\16-02-2023\folder_test\text\*'
    sub_folders = glob.glob(folder_path)
    the_lastest_subfolder = max(sub_folders, key=os.path.getctime)
    files = glob.glob(the_lastest_subfolder + '\*')
    the_last_file = max(files, key=os.path.getctime)
    print(the_last_file)
    type = the_last_file.split('.')[1]
    if type == 'mp3':
        mp3_path = the_last_file
        wav_path = the_last_file.split('.')[0] + '.wav'
        sound = pydub.AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        print(wav_path)
        return wav_path
    elif type == 'wav':
        return the_last_file
    else:
        return False
    
def wav_to_txt(wav):
    r = sr.Recognizer()
    with sr.AudioFile(wav) as source:
        audio = r.record(source)
        text = r.recognize_google(audio, language = "vi-VI")
        with open('log.txt', mode = 'a', encoding = 'UTF-8', errors = 'ignore') as data:
            data.write(str(text))

def split_list_answer():
    col_answer = []
    with open("log.txt","r", encoding="UTF-8") as f:
        ot = f.read()       #original text
    for j in ot.split('bắt đầu'):
        answer = j.split('thời')[0].strip()[-1]
        col_answer.append(answer.upper())
    col_answer.pop(0)
    

          
t = mp3_to_wav()
wav_to_txt(t)
split_list_answer() 
