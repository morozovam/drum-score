#!/bin/bash
cd /app/backend/
pip install --upgrade pip pip-tools
pip-compile --output-file=requirements.txt pyproject.toml
pip-compile --extra=dev --output-file=dev-requirements.txt pyproject.toml
