#!/bin/bash
cd /app/
apt-get update && apt-get install jq -y
export $(cat .version)
sed -i 's/^version = ".\{1,\}"/version = "'$version'"/'  backend/pyproject.toml
jq  '.version = "'$version'"' frontend/drum-score/package.json > frontend/drum-score/package.json.tmp && \
mv --backup=simple --suffix=.old -v frontend/drum-score/package.json.tmp frontend/drum-score/package.json 
jq  '.version = "'$version'"' frontend/drum-score/package-lock.json | jq '.packages."".version = "'$version'"'> frontend/drum-score/package-lock.json.tmp &&\
mv --backup=simple --suffix=.old -v frontend/drum-score/package-lock.json.tmp frontend/drum-score/package-lock.json