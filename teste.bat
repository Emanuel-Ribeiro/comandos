@echo off

color 2

if "%1" == "" goto lista comandos
if "%1" == "fav" goto favoritos
if "%1" == "web" goto web
if "%1" == "local" goto local

goto erro

:lista comandos
echo Lista de comandos: 
echo .
echo ---------------------------------------------
echo I 	  fav 	 - abre sites favoritos          I
echo I                                           I
echo I    web    - cria um projeto no htdocs     I
echo I                                           I
echo I   local  - cria um projeto nos documentos I
echo ---------------------------------------------
echo .
goto fim

:favoritos

start https://mail.google.com/mail/u/1/#inbox
start https://outlook.live.com/mail/0/inbox
start https://www.youtube.com
start https://www.kabum.com.br
goto fim

:local

cd C:\Users\Emanuel\Documents
start C:\Users\Emanuel\comandos\criarProjetoLocal.py
goto fim

:web

cd cd C:\xampp\htdocs
start C:\Users\Emanuel\comandos\criar.py
goto fim

:erro

echo comando invalido!
goto fim

:fim