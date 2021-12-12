@echo off
setlocal enabledelayedexpansion
set "string="
set /p co=co: 
set /p naco=naco: 
for /f "tokens=* delims=" %%i in (%1) do (
set string=!string!%%i
set string=!string:%co%=%naco%!
)
echo %string% > %2
pause