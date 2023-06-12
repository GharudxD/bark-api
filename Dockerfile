FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 9000

CMD [ "python3", "main.py" ]