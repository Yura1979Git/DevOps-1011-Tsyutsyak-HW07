FROM python:3.8-alpine3.16

WORKDIR /app

EXPOSE 5000

COPY ["requirements.txt", "./"]
RUN pip3 install -r requirements.txt

COPY ["app.py", "./"]

CMD [ "python3", "./app.py"]
