@echo off
:x
echo 1.program
echo 2.instrukcje
echo 3.backup
echo 4.exit
set /p wybor=Wybierz opcje: 
if %wybor% equ 1 goto start
if %wybor% equ 2 goto info
if %wybor% equ 3 goto backup
if %wybor% equ 4 exit
else goto x
:start
cls 
python main.py
python createSite.py
start raport\result.html
goto x
:info
cls
echo Karol Cieply odwrocona piramida
echo Program wypisuje kolejne wyrazy z slownika usuwajac za każdym razem jedna litere
goto x
:backup
if not exist backup\ (
    mkdir backup
)
cls
set date=%date:~-0,4%%date:~4,2%%date:~6,4%
if exist backup\%date% (
    echo "Robiles juz dzisiaj backup"
) else (
    mkdir backup\%date%
    copy *.* backup\%date%\
)

goto x