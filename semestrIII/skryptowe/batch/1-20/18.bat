@echo off
forfiles /m *.txt /c "cmd /c attrib +a @path"
pause