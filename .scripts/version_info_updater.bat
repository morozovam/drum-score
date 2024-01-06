@echo off
set DRUMSCORE_VERSION=%1
echo Set version to %DRUMSCORE_VERSION%
pause
docker run --rm -it --env DRUMSCORE_VERSION=%DRUMSCORE_VERSION% -v %CD%:/app/  debian /app/.scripts/version_info_updater.sh
pause