@echo off
cd %1
ren *.txt *.tmp
echo czy chcesz skopiować?
set /p b=(t/n)?: 
if b equ t(
    set /p path=podaj katalog
    set /p date=podaj jak stare pliki (w dniach)
    forfiles /m *.tmp /d -%date% /c "cmd /c copy %path%\@file"
)
pause