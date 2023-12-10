To update version info in project files edit .version and run following command in root:

docker run -it -v ${PWD}:/app  debian /app/.scripts/version_info_updater.sh