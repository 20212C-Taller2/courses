# Dockerfile

# pull the official docker image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# set work directory
WORKDIR /app

# set env variables

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /app
