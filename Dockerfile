FROM python:3.8-alpine3.16

RUN adduser --disabled-password webapp && apk --no-cache add curl

ENV USER="${USER}" REDIS_HOST="$REDIS_HOST" REDISPORT="$REDIS_PORT"

ARG APP_VERSSION BUILD_NUMBER

LABEL tyi.app.version="${APP_VERSSION}" \
      tyi.app.build="${BUILD_NUMBER}" \
      tyi.app.vendor="TYI" \
      tyi.app.description="Simple Python Flask app with Redis"

USER webapp

WORKDIR /app

EXPOSE 5000

COPY ["requirements.txt", "./"]
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ["./templates/*", "/templates/"]
COPY ["app.py", "./"]

ENTRYPOINT [ "python3" ]

CMD [ "./app.py"]
