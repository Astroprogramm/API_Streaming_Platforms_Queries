
FROM tiangolo/uvicorn-gunicorn:python3.8

COPY requirements.txt //requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload

COPY ./app /app
