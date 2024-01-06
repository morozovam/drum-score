#!/bin/bash
cd /app/
echo Set version: $DRUMSCORE_VERSION
if [[ -z "${DRUMSCORE_VERSION}" ]]; then
    echo env DRUMSCORE_VERSION is empty, will be used .version file
    export $(cat .version)
else
    echo DRUMSCORE_VERSION=$DRUMSCORE_VERSION > ./.version
fi
echo Install jq to edit package.json and package-lock.json files
apt-get update && apt-get install jq -y
echo Editing backend/pyproject.toml
sed -i 's/^version = ".\{1,\}"/version = "'$DRUMSCORE_VERSION'"/'  backend/pyproject.toml
echo Editing frontend/drum-score/package.json
jq  '.version = "'$DRUMSCORE_VERSION'"' frontend/drum-score/package.json > frontend/drum-score/package.json.tmp && \
mv --backup=simple --suffix=.old -v frontend/drum-score/package.json.tmp frontend/drum-score/package.json 
echo Editing frontend/drum-score/package-lock.json
jq  '.version = "'$DRUMSCORE_VERSION'"' frontend/drum-score/package-lock.json | jq '.packages."".version = "'$DRUMSCORE_VERSION'"'> frontend/drum-score/package-lock.json.tmp &&\
mv --backup=simple --suffix=.old -v frontend/drum-score/package-lock.json.tmp frontend/drum-score/package-lock.json
echo Done!