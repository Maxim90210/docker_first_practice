FROM python:3.11.6-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . .

RUN echo "Hello from installing"
RUN apt-get upgrade

CMD ["python", "main.py"]