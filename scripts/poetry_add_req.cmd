@echo off

for /f "tokens=*" %%i in (../requirements.txt) do ( poetry add --lock %%i )

rem FOR /F "usebackq delims=" %G IN (../requirements.txt) DO poetry add --lock %G