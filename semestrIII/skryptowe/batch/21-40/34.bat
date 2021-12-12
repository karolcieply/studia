@echo off
set /p x=Podaj katalog docelowy: 
set /p y=Podaj plik docelowy: 
call 31.bat %x%
dir %x% > %y%