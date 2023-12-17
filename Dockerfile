FROM python:3.12.1

RUN mkdir "/task_manager"

WORKDIR /task_manager

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
