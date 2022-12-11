from fastapi import FastAPI, Path, UploadFile, File
from typing import Optional
from pydantic import BaseModel
import shutil
import pandas as pd
from fastapi.responses import HTMLResponse

app=FastAPI()

Data_file = UploadFile('Data.json')

@app.on_event('startup')
async def startup():
	global DATA
	DATA = pd.read_json('Data.json')
	
@app.get('/get_max_duration/{year},{platform},{min_season}')
async def get_max_duration(year:int,platform:str,min_season:str):
	id_max_duration = DATA[(DATA.release_year==year) | (DATA.Platform==platform) | (DATA.duration_type==min_season)]
	max_title= id_max_duration.title.loc[id_max_duration['duration_quantity'].idxmax()]
	return max_title

@app.get('/get_count_plataform/{platform}')
async def get_count_plataform(platform:str):
	data_platform = DATA[DATA.Platform==platform]
	films = data_platform[data_platform.duration_type=='min']
	series = data_platform[data_platform.duration_type=='season']
	response = {'Plaform': platform,
             'Movies': films.shape[0],
             'Series': series.shape[0]}
	return response

@app.get('/get_listedin/{listed}')
async def get_count_plataform(listed:str):
	#Preparing the data to filter by each platform
	Amazon_data = DATA[(DATA.Platform=='Amazon')]
	Amazon= Amazon_data[Amazon_data.listed_in.str.contains(listed)]

	Disney_data = DATA[(DATA.Platform=='Disney')]
	Disney = Disney_data[Disney_data.listed_in.str.contains(listed)]

	Hulu_data = DATA[(DATA.Platform=='Hulu')]
	Hulu = Hulu_data[Hulu_data.listed_in.str.contains(listed)]

	Netflix_data = DATA[(DATA.Platform=='Netflix')]
	Netflix = Netflix_data[Netflix_data.listed_in.str.contains(listed)]
	
	#Getting the information we need:
	repeated=int(Amazon.shape[0])
	Sites=['Amazon','Disney','Hulu','Netflix']
	count=0
	index_platform=0
	for i in [Amazon,Disney,Hulu,Netflix]: #Iterating in every platform
	  if int(i.shape[0])>repeated:
	    repeated=i.shape[0]	#Maximum number of appereance of the genre
	    uni=index_platform		#To get in which platform the genre appears the most
	  count+=1
	response = {'Plaform': Sites[index_platform],
	     'Quantity': repeated}
	return response
	
	
	
	
	
