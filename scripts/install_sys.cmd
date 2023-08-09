@echo off
PUSHD ..
pip install .
echo .
pip list |find "assistant-bot"
echo .
echo Package installed to PATH where placed your system Python ('...\local-packages\Python311\Scripts')
echo Now can run packege by run "assistant_bot"
echo help for run of assistant_bot aviable via runtime parameter -h, for example "assistant_bot -h"
POPD
pause