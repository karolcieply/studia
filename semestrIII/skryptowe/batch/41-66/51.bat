@echo off
set /p a=Podaj pierwsza liczbe:
set /p b=Podaj druga liczbe:
echo 1:dodawanie
echo 2:odejmowanie
echo 3:mnozenie
echo 4:dzielenie
set /p d=Wybierz Liczbe
if %d% equ 1 (set /a a=%a%+%b%)
if %d% equ 2 (set /a a=%a%-%b%)
if %d% equ 3 (set /a a=%a%*%b%)
if %d% equ 4 (set /a a=%a%/%b%)
echo Wynik: %a%
pause