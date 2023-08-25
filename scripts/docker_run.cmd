@echo off
PUSHD ..\tests

docker run --rm --name assistant-bot_once -it lexxai/assistant-bot 

POPD
