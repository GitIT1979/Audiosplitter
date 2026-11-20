@echo off
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python не найден. Установите Python 3 или откройте AudioSplitter.html напрямую.
  pause
  exit /b 1
)
python serve.py
pause
