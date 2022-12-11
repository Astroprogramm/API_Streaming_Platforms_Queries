# Individual Project 1
First individual project develop in Henry, with focus in Data Engineering (ETL)

This repository presents an ETL done in datasets of movies and series from 4 different platforms: Amazon, Disney Plus, Hulu and Netflix. You can find the notebook where the ETL was performed in the folder named 'Dataset_and_ETL' with description of the process, and you can also find in the same folder the final dataset ready for queries in JSON format. The notebook also contains some of the code used to performe the queries in an docker container with FastAPI, Uvicorn and Tiangolo.

In the folder 'FastAPI_Docker' you can find all the files necessary to run a FastAPI with uvicorn and tiangolo, which performs the following queries:

+ Maximum duration according to film type (film/series), platform and year. The request is: get_max_duration(year, platform, [min or season])

+ Number of films and series (separate) per platform. Request is: get_count_plataform(platform)  
  
+ The number of times a genre and platform is repeated most often. The request is: get_listedin('genre').

+ Actor that most repeats according to platform and year. The request is: get_actor(platform, year)


In order to use the API you must input _genre_ and _platform_ values with initial uppercase (example: Comedy, Amazon), and the values min or season all in lower case (example: min, season). You can use this API passing the values as the examples below:
http://127.0.0.1:8000/get_actor/Netflix,2020
http://127.0.0.1:8000/get_max_duration/2018,Amazon,min
