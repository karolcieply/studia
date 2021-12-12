@echo off
set /p ile=ile liczb?
for /l %%i in (1,1,%ile%) do echo %%i >> %1
pause