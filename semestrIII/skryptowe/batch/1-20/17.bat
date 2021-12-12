@echo off
cd %userprofile%
forfiles /m *.txt /c "cmd /c type @path >> plikpolaczony.txt"
pause