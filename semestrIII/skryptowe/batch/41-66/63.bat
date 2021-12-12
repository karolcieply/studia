@echo off
echo 1.program
echo 2.instrukcje
echo 3.backup
echo 4.exit
:x
set /p wybor=[wybierz opcje]
if %wybor% equ 1 goto start
if %wybor% equ 2 goto info
if %wybor% equ 3 goto backup
if %wybor% equ 4 exit
else goto x
:start
cls 
python main.py
goto x
:info
cls
echo Karol Cieply odwrocona piramida
goto x
:backup
cls
goto x