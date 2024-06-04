FROM python:latest

RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



EXPOSE 3000

CMD ["python", "src/app.py"]
