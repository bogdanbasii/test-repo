FROM python:3.11

WORKDIR /data

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 4200

