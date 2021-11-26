FROM python:3.10.0-alpine

WORKDIR /app

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:5000 -w 4 -k 'gthread' --threads 2 run:app