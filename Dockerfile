FROM python:3.9
WORKDIR /code
COPY ./ /code
#COPY requirements.txt /code/requirements.txt
#COPY main.py /code/main.py
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

#COPY requirements.txt /tmp/requirements.txt
#RUN python3 -m pip install -r /tmp/requirements.txt

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload

#COPY ./app /app
