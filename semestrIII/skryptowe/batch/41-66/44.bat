@echo off
set /p typ=jaki typ?
if exist *.%typ% (del *.%typ%) else (echo nie ma takiego pliku)
pause