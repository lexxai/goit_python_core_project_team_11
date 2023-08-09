@echo off
PUSHD ..
IF exist .venv (
CALL .venv\Scripts\activate
pip uninstall assistant_bot
pip list |find "assistant-bot"
deactivate
echo .
echo DONE
)
POPD
pause