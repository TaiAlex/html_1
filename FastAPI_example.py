from fastapi import File, UploadFile, Request, FastAPI
from fastapi.templating import Jinja2Templates
import str_time
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

time = str_time.now_utc()
dir_name = str_time.str_yyyy_mm_dd(time)
file_name = str_time.get_time()

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        # contents = file.file.read()
        # with open("uploaded_" + file.filename, "wb") as f:
        #     f.write(contents)
        dir_path = "upload/" + str_time.str_yyyy_mm_dd(time)
        # str_time.create_path("upload")
        str_time.create_path(dir_path)
        type = file.filename.split(".")[1]
        file_path = dir_path + "/" + f'{file_name}.{type}'
        text_path = os.path.join(os.path.dirname(__file__), f'{file_name}.{type}')
        # print('target_path_1: ', text_path)
        # print(file_path)
        file_bytes = file.file.read()
        # print(file_bytes)
        str_time.upload_file_bytes(file_bytes, file_path)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()   
    return {"message": f"Successfuly uploaded {file.filename}"}

@app.get("/to_text")
def display_text():
    with open('log.txt', 'r', encoding='UTF-8') as alex:
        t = alex.read()
    return {'Hello': t}

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("template.html", {"request": request})
