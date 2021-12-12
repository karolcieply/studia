@echo off
set /p n=ile liczb?
for /l %%i in (1,1,%n%) do (echo %%i>>%1)
pause