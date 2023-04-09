@echo off
cd src
:START
cls
echo Running 'py run.py gen' command......
echo Generating......
py run.py gen

:CHOOSE
set /p type= "[1] for test CheckerSuite      [4] for clean generated files .              "
if '%type%'=='1' echo Running test CheckerSuite......
if '%type%'=='1' py run.py test CheckerSuite

if '%type%'=='4' echo Cleanning 'target' folder......
if '%type%'=='4' del ..\target\* /q

set /p choice= "Press 'Enter' to restart or 'n' for Exit:          "
if '%choice%'=='' goto START
if '%choice%'=='n' exit
