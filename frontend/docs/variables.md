# Variables description:

## Variables used in docker container

Path where staticfiles and mediafiles should be mounted:
```
APP_HOME=/home/app/web 
```
Name or IP address of backend container. Useful in docker compose.
```
DRUMSCORE_BACKEND_ADDRESS=localhost
```
Backend container port.
```
DRUMSCORE_BACKEND_PORT=8000
```
Port whitch nginx should listern.
``` 
DRUMSCORE_FRONTEND_PORT=80
``` 
Maximum upload size limited by client_max_body_size in default.conf in nginx config file.
```
DRUMSCORE_MAX_UPLOAD_SIZE=40M
```
