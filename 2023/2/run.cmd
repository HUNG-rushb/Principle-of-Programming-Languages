@echo off
cd src
:START
cls
echo Running 'py run.py gen' command......
echo Generating......
py run.py gen

:CHOOSE
set /p type= "[1] for test LexerSuite. [2] for test ParserSuite. [3] for test AST         [4] for clean generated files .              "
if '%type%'=='1' echo Running test LexerSuite......
if '%type%'=='1' py run.py test LexerSuite

if '%type%'=='2' echo Running test ParserSuite......
if '%type%'=='2' py run.py test ParserSuite

if '%type%'=='3' echo Running test ASTGenSuite......
if '%type%'=='3' py run.py test ASTGenSuite

if '%type%'=='4' echo Cleanning 'target' folder......
if '%type%'=='4' del ..\target\* /q

set /p choice= "Press 'Enter' to restart or 'n' for Exit:          "
if '%choice%'=='' goto START
if '%choice%'=='n' exit
