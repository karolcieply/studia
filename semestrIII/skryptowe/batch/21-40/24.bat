@echo off
mkdir backup
xcopy %1 backup /s /d %2
pause