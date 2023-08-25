@echo off
PUSHD ..

docker build . -t lexxai/assistant-bot
docker images

POPD
