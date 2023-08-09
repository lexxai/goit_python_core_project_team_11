@echo off
PUSHD ..
pip uninstall assistant_bot
pip list |find "assistant-bot"
echo .
echo DONE
POPD
pause