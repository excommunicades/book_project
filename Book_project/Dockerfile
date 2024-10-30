FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY reqs.txt /app/
RUN pip install --no-cache-dir -r reqs.txt

COPY . /app/
