REM @echo off
PUSHD ..
IF not exist .venv (python -m venv .venv)
CALL .venv\Scripts\activate

pip install .

echo .
pip list |find "assistant-bot"
echo .
echo Package installed to PATH where placed virual system Python ('.venv\Scripts')
echo Now can run packege by run "assistant_bot" into .venv enviroment.
echo help for run of assistant_bot aviable via runtime parameter -h, for example "assistant_bot -h"
POPD
pause