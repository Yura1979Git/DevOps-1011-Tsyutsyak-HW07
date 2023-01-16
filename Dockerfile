FROM python:3.8-alpine3.16

RUN adduser --disabled-password webapp

WORKDIR /app

EXPOSE 5000

COPY ["requirements.txt", "./"]
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ["app.py", "./"]

USER webapp

ENTRYPOINT [ "python3" ]

CMD [ "./app.py"]
