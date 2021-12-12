@echo off
cd C:\
forfiles /m *.exe /s /c "cmd /c echo @path"
pause