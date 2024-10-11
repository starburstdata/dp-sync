#!/usr/bin/env bash
#must rename root dir to python for lambda
if [ $(basename "${PWD}") != "dp-sync" ]; then
  echo 'Must run from dp-sync directory'
  exit 1
fi
pip list --format=freeze | grep -v setuptools | grep -v pip | grep -v wheel > requirements.txt
cd ..
rm -rf python && cp -R dp-sync python && cd python
pip install -r requirements.txt --target .
find . -name '*.pyc' -delete
rm -rf secret.squirrel galaxy_swagger_client sep_swagger_client .git .idea  .gitignore step-function
rm -rf README.md runner.py zip-lambda-layer.sh
rm -rf __pycache__ ./*/__pycache__ ./*/*/__pycache__ ./*/*/*/__pycache__
cd ..
rm dp-sync-deps-layer.zip
zip -r dp-sync-deps-layer.zip python
