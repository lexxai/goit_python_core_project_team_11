@echo off
PUSHD ..\tests

   
docker run -it --rm  -v user_data:/app/user_data --name assistant-bot_volume  lexxai/assistant-bot                                 


POPD
