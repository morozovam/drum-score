FROM python:3.11-alpine as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN apk update && \
    apk add --virtual build-deps gcc &&\
    pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt &&\
    apk del build-deps

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-index --find-links=/wheels/ -r requirements.txt &&\
    rm -R /wheels
COPY . .
COPY --chmod=a+rx dockerfiles/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
RUN mkdir "files" &&\
    mkdir "./files/static" &&\
    mkdir "./files/media"
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=5s --start-period=5s --retries=5 CMD [ "wget --no-verbose --tries=1 --spider http://localhost:8000/api/v1/ || exit 1" ]