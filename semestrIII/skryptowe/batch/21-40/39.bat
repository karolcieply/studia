@echo off
call 37.bat
mkdir eps
copy *.eps /eps
cd eps
dir /b > plikigraficzne.txt
pause
