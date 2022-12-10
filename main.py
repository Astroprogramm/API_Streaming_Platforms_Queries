from fastapi import FastAPI, Path, UploadFile, File
from typing import Optional
from pydantic import BaseModel
import shutil

app=FastAPI()

@app.get('/get_max_duration({year},{platform},{type})')
async def get_max_duration():
    return {'name':'First Data'}

