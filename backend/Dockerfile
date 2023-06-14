FROM python:3.10.12-slim-bullseye
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000