@echo off
setlocal enabledelayedexpansion
set /p plik1=plik1: 
set /p plik2=plik2:
set "string="
for /f "tokens=* delims=" %%i in (%plik1%) do (
set string=!string!%%i
)
set string=!string!
for /f "tokens=* delims=" %%i in (%plik2%) do (
set string=!string!%%i
)
echo %string%
pause