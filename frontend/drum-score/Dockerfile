#STAGE 1
FROM node:20.10-alpine AS build
RUN mkdir /app
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

#STAGE 2
FROM nginx:1-alpine-slim
RUN rm -rf /usr/share/nginx/html/* &&\
    rm -rf /etc/nginx/templates/* &&\
    rm -rf /etc/nginx/conf.d/*     
ENV HOME=/home/app \
    APP_HOME=/home/app/web \
    DRUMSCORE_BACKEND_ADDRESS=localhost \
    DRUMSCORE_BACKEND_PORT=8000 \
    DRUMSCORE_FRONTEND_PORT=80 \
    DRUMSCORE_MAX_UPLOAD_SIZE=40M
RUN mkdir $HOME &&\
    mkdir $APP_HOME &&\
    mkdir $APP_HOME/staticfiles &&\
    mkdir $APP_HOME/mediafiles
COPY dockerfiles/default.conf.template /etc/nginx/templates/default.conf.template
COPY dockerfiles/favicon /usr/share/nginx/html/favicon
COPY --from=build /app/dist/drum-score /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=10s --timeout=5s --start-period=5s --retries=5 CMD [ "wget --no-verbose --tries=1 --spider http://localhost/ || exit 1" ]