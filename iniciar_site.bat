@echo off
title Vitrine de Afiliados - Achadinhos
echo ========================================================
echo       INICIANDO SUA VITRINE DE AFILIADOS
echo ========================================================
echo.
echo Abrindo o navegador em http://localhost:5000 ...
start http://localhost:5000
echo.
echo IMPORTANTE: Deixe esta janela aberta enquanto estiver usando o site!
echo Para desligar o site, basta fechar esta janela ou teclar Ctrl + C.
echo.
cd /d "C:\Users\joaoh\.gemini\antigravity\scratch\vitrine-afiliados"
python app.py
pause
