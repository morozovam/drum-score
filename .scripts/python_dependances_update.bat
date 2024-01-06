@echo off
echo Start scipt
echo Current path: %CD%
echo Should run at root folder of project
pause
CHDIR %CD%\backend\
echo Making requirements.txt
pip-compile --output-file=requirements.txt pyproject.toml
echo Making dev-requirements.txt 
pip-compile --extra=dev --output-file=dev-requirements.txt pyproject.toml
echo done!
pause