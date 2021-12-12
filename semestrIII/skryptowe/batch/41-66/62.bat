@echo off
setlocal enabledelayedexpansion
set "string="
for /f "tokens=* delims=" %%i in (%1) do (
set string=!string!%%i
set string=!string:"=!
)
echo %string%
pause