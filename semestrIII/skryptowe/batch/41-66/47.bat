@echo off
if %1 equ create type NUL>test.txt
if %1 equ delete del test.txt
pause