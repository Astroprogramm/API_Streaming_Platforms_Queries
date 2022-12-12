# Individual Project 1
First individual project develop in Henry, with focus in Data Engineering (ETL)

This repository presents an ETL done in datasets of movies and series from 4 different platforms: Amazon, Disney Plus, Hulu and Netflix. You can find the notebook where the ETL was performed in the folder named 'Dataset_and_ETL' with description of the process, and you can also find in the same folder the final dataset ready for queries in JSON format. The notebook also contains some of the code used to perform the queries in a docker container with FastAPI, Uvicorn and Tiangolo.

Here you can find all the files necessary to run a FastAPI with uvicorn and tiangolo, which performs the following queries:

+ Maximum duration according to film type (film/series), platform and year. The request is: get_max_duration(year, platform, [min or season])

+ Number of films and series (separate) per platform. Request is: get_count_plataform(platform)

+ The number of times a genre and platform where is repeated most often. The request is: get_listedin(genre).

+ Actor that most repeats according to platform and year. The request is: get_actor(platform, year)

In order to use the API you must input _genre_ and _platform_ values with initial uppercase (example: Comedy, Amazon), and the values min or season all in lower case (example: min, season).

If you want to run this docker locally, you use the API passing the values as the examples below:

http://127.0.0.1:8000/get_max_duration/2018,Hulu,min

http://127.0.0.1:8000/docs

The API was also deployed using Mogenius, and can be accessed like this:

https://query-app-prod-query-api-fxqxpr.mo5.mogenius.io/docs

https://query-app-prod-query-api-fxqxpr.mo5.mogenius.io/get_max_duration/2018,Hulu,min

________________________

# Proyecto individual 1
Primer proyecto individual desarrollado en Henry, con enfoque en Ingeniería de Datos (ETL)

Este repositorio presenta un ETL hecho en datasets de películas y series de 4 plataformas diferentes: Amazon, Disney Plus, Hulu y Netflix. Puede encontrar el notebook donde se realizó el ETL en la carpeta llamada 'Dataset_and_ETL' con la descripción del proceso, y también puede encontrar en la misma carpeta el dataset final para consultas en formato JSON. El notebook también contiene parte del código utilizado para realizar las consultas en un contenedor acoplable con FastAPI, Uvicorn y Tiangolo.

Aquí puedes encontrar todos los archivos necesarios para ejecutar un FastAPI con uvicorn y tiangolo, que realiza las siguientes consultas:

+ Duración máxima según tipo de película (película/serie), plataforma y año. La solicitud es: get_max_duration(año, plataforma, [min o seasons])

+ Número de películas y series (por separado) por plataforma. La solicitud es: get_count_plataform(plataforma)  
  
+ El número de veces que se repite un género y la plataforma dónde más se repite. La petición es: get_listedin('género').

+ Actor que más se repite según la plataforma y el año. La petición es: get_actor(plataforma, año)


Para utilizar la API debe introducir valores _genero_ y _plataforma_ con mayúsculas iniciales (ejemplo: Comedy, Amazon), y los valores min o season en minúsculas (ejemplo: min, season). Si desea correr este docker localmente puede hacerlo pasando así los parámetros:

http://127.0.0.1:8000/get_max_duration/2018,Hulu,min

http://127.0.0.1:8000/docs

También fue hecho un deployment utilizando Mogenius, se puede acceder de la siguiente manera:
https://query-app-prod-query-api-fxqxpr.mo5.mogenius.io/docs

https://query-app-prod-query-api-fxqxpr.mo5.mogenius.io/get_max_duration/2018,Hulu,min


