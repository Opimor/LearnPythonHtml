@echo off
cd /d %~dp0
start "" pythonw app.py
timeout /t 2 >nul
start "" http://localhost:5000
echo Learn Python запущен: http://localhost:5000
pause