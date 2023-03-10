# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import FastAPI, File, UploadFile, APIRouter, Request
# from fastapi.responses import HTMLResponse, StreamingResponse
# from fastapi.templating import Jinja2Templates
# from typing import List
# import pandas as pd
# import shutil as st
# import str_time
# import os
# import filetype
# templates = Jinja2Templates(directory="templates")

# app = FastAPI()
# time = str_time.now_utc()
# dir_name = str_time.str_yyyy_mm_dd(time)
# file_name = str_time.get_time()
# origins = [
#    "http://localhost",
#    "http://localhost:8000",
# ]
# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
# )




# @app.get("/")
# async def main():
#    return {"message": "Hello World"}

# @app.post("/uploadfile/")
# async def upload_file(files: List[UploadFile] = File(...)):
#   for file_in_list in files:
#     dir_path = "upload/" + str_time.str_yyyy_mm_dd(time)
#     str_time.create_path("upload")
#     str_time.create_path(dir_path)
#     type = file_in_list.filename.split(".")[1]
#     file_path = dir_path + "/" + f'{file_name}.{type}'
#     file_bytes = file_in_list.file.read()
#     str_time.upload_file_bytes(file_bytes, file_path)
#     # with open(f'{file_path}', 'wb') as alex:
#     #     st.copyfileobj(file_in_list.file, alex)
#     return {'file_name': file_in_list.filename}

# @app.get("/", response_class=HTMLResponse)
# def main(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})





#test get method with a text file

# from fastapi import FastAPI
# from typing import Union
# from fastapi.responses import FileResponse

# @app.get("/")
# def read_root():
#    with open('test1.txt', 'r') as alex:
#       t = alex.read()
#    return {"Hello": t}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}



import speech_recognition as sr
from os import path
# from pydub import AudioSegment
import pydub

# # files                                                                         
src = r"E:\04-02-2023\folder1\ulatroi.mp3"
dst = r"E:\04-02-2023\folder1\ulatroi.wav"
# dst = r"E:\04-02-2023\folder1\ulatroi.wav"

# # convert wav to mp3                                                            
# sound = pydub.AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

import os
import pydub
import glob

# target_path_1 = os.path.join(os.path.dirname(__file__), 'log.txt')

# print('target_path_1: ', target_path_1)

# print('read target file:')
# with open(target_path_1, encoding='UTF-8') as f:
#     print(f.read())

def find_path():
#     folder_path = r'E:\16-02-2023\folder_test\text\*'
    folder_path = r'/home/ubuntu/html_1*'
    sub_folders = glob.glob(folder_path)
    the_lastest_subfolder = max(sub_folders, key=os.path.getctime)
    files = glob.glob(the_lastest_subfolder + '/*')
    the_last_file = max(files, key=os.path.getctime)
    print(the_last_file)
    return the_last_file

mp3_to_wav(find_path())

def mp3_to_wav(file_path):
    type = file_path.split('.')[1]
    if type == 'mp3':
        mp3_path = file_path
        wav_path = file_path.split('.')[0] + '.wav'
        sound = pydub.AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        print(wav_path)
        return wav_path
    elif type == 'wav':
        return file_path
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
    for j in ot.split('b???t ?????u'):
        answer = j.split('th???i')[0].strip()[-1]
        col_answer.append(answer.upper())
    col_answer.pop(0)
    print(col_answer)           

mp3_to_wav(find_path())
