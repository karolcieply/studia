@echo off
if %1 equ /h (
    echo Program usuwa wpisy z podmenu autostartu i wpisy z rejestru
    echo odpowiedzielne za wlaczanie programow przy starcie 
    echo /a usun bez pytania 
    echo /h-wyswietl pomoc
    goto end
)
if %1 equ /a(
    del “%USERPROFILE%\MenuStart\Programy\Autostart\*.*” /f
    reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run” /va /f
    goto end
)

%USERPROFILE%\MenuStart\Programy\Autostart\*.*” /p 
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run” /va

:end
pause