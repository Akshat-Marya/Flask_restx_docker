FROM python:3

RUN apt-get update && apt-get install -y

COPY ./ /home/acerta_challenge
WORKDIR /home/acerta_challenge

RUN pip install -r requirements.txt
RUN python create_db.py
EXPOSE 5000
ENTRYPOINT python run.py

