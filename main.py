from fastapi import FastAPI, UploadFile
from feature import file

app = FastAPI()

app.include_router(file.router)