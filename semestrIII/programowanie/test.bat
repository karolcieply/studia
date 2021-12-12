@echo off
set string=
set a=31
:loop
set /a reszta=a%%2
set /a a=%a%/2
set string=%reszta%%string%
if %a% equ 0 goto x
goto loop
:x
echo %string%
echo a teraz poczytaj z dolu do gory
