from fastapi import FastAPI, Path, UploadFile, File
from typing import Optional
from pydantic import BaseModel
import shutil
import pandas as pd

app=FastAPI()

@app.on_event('startup')
async def startup():
	global DATA
	DATA = pd.read_json('Data.json')
	
@app.get('/get_max_duration/{year},{platform},{min_season}')
async def get_max_duration(year:int,platform:str,min_season:str):
	id_max_duration = DATA[(DATA.release_year==year) & (DATA.Platform==platform) & (DATA.duration_type==min_season)]
	if id_max_duration.shape[0]!=0:
		max_title= id_max_duration.title.loc[id_max_duration['duration_quantity'].idxmax()]
		response = {'Title': max_title}
	else:
		response = 'No data available'
	return response

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
	Amazon = DATA[(DATA.Platform=='Amazon') & (DATA.listed_in.str.contains(listed))]

	Disney = DATA[(DATA.Platform=='Disney') & (DATA.listed_in.str.contains(listed))]

	Hulu = DATA[(DATA.Platform=='Hulu') & (DATA.listed_in.str.contains(listed))]

	Netflix = DATA[(DATA.Platform=='Netflix')& (DATA.listed_in.str.contains(listed))]
	
	#Getting the information needed:
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
	

@app.get('/get_actor/{platform},{year}')
async def get_actor(platform:str,year=int):
	data_act = DATA[(DATA.release_year==year) & (DATA.Platform==platform)]
	if data_act.shape[0]!=0:
		act = data_act.cast.mode()
		reps = data_act.cast.value_counts()[0]
		response = {'Plaform': platform,
	     		'Quantity': int(reps),
	     		'Actors': act[0]}
	else:
		response = 'No data available'
	return response, data_act.shape[0]
	
	
	
	
