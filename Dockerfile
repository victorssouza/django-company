FROM python:3.6-alpine

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD ["./startup.sh"]