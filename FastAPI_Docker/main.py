from fastapi import FastAPI, Path, UploadFile, File
from typing import Optional
from pydantic import BaseModel
import shutil
import pandas as pd

app=FastAPI()

Data_file = UploadFile('Data.json')

@app.on_event('startup')
async def startup():
	global DATA
	DATA = pd.read_json('Data.json')
	
#{year},{platform},{type}
@app.get('/get_max_duration/{year},{platform},{min_season}')
async def get_max_duration(year:int,platform:str,min_season:str):
	id_max_duration = DATA[(DATA.release_year==year) | (DATA.Platform==platform) | (DATA.duration_type==min_season)]
	max_title= id_max_duration.title.loc[id_max_duration['duration_quantity'].idxmax()]
	return max_title

