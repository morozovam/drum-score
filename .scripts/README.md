# Managment scripts

## Update version info:

To update version info in project files edit .version set env ${DRUMSCORE_VERSION}  and run following command in root project folder:
```
docker run --rm -it --env DRUMSCORE_VERSION=${DRUMSCORE_VERSION} -v ${PWD}:/app  debian /app/.scripts/version_info_updater.sh
```
or run script with disired version as first param:
```
.\.scripts\version_info_updater.bat ${DRUMSCORE_VERSION}
```

 ## Update dependances
 For Linux:

 ```
 docker run --rm -it -v ${PWD}:/app  python:3.11 /app/.scripts/python_dependances_update.sh
 ```
 For Windows:
 ```
 .\.scripts\python_dependances_update.bat
 ```