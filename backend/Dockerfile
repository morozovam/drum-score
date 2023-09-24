FROM python:alpine as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN apk update && \
    apk add --virtual build-deps gcc &&\
    pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt &&\
    apk del build-deps

FROM python:alpine
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-index --find-links=/wheels/ -r requirements.txt &&\
    rm -R /wheels
COPY . .
RUN mkdir "files" &&\
    mkdir "./files/static" &&\
    mkdir "./files/media"
COPY dockerfiles/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+rx /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8000
