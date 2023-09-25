#STAGE 1
FROM node:18.15-alpine AS build
RUN mkdir /app
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

#STAGE 2
FROM nginx:1-alpine-slim
RUN rm -rf /usr/share/nginx/html/*
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
COPY dockerfiles/nginx.conf.template /nginx.conf.template
COPY dockerfiles/favicon /usr/share/nginx/html/favicon
COPY --from=build /usr/src/app/dist/drum-score /usr/share/nginx/html
CMD ["/bin/sh" , "-c" , "export DRUMSCORE_BACKEND && envsubst '$$DRUMSCORE_BACKEND' < /nginx.conf.template > /etc/nginx/nginx.conf && exec nginx -g 'daemon off;'"]
EXPOSE 80
