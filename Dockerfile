From python:3.14.0a3-alpine

WORKDIR /app

COPY requirements.txt .
COPY . . 

RUN pip install -r requirements.txt

CMD [ "python","app.py"]