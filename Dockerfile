FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

# serve the app / run the app (keep it running)

CMD ["python","run.py"]
