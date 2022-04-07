FROM python:3.9-slim-buster

ENV DSW_CONFIG /app/config.yml
ENV SEEDER_WORKDIR /app/data
ENV SEEDER_RECIPE example

WORKDIR /app

RUN mkdir -p /app/data

RUN apt-get update && apt-get install -qq -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
RUN pip install .

CMD ["dsw-seeder", "run"]
