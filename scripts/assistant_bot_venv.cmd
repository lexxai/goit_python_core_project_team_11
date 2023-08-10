@echo off
PUSHD ..
IF exist .venv (
CALL .venv\Scripts\activate
assistant_bot %*    
)
POPD
pause
