@echo off
PUSHD ..\tests

rem docker rm -f assistant-bot 
rem docker run --name assistant-bot --entrypoint /bin/bash   lexxai/assistant-bot 
docker create -it --name assistant-bot lexxai/assistant-bot
docker start -i assistant-bot                                       


POPD
