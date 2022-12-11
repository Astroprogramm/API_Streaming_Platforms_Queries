
FROM tiangolo/uvicorn-gunicorn:python3.8

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload

#COPY ./app /app
