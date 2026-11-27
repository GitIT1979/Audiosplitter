@echo off
rem Пересборка десктопной версии: копирует актуальные файлы HTML-версии в resources/app.
rem Рантайм Electron должен быть распакован в папку AudioSplitter (AudioSplitter.exe на месте).
rem Если папки AudioSplitter нет — см. README-DESKTOP.md (как скачать и распаковать рантайм).
cd /d "%~dp0"
if not exist "AudioSplitter\AudioSplitter.exe" (
    echo Папка AudioSplitter с рантаймом Electron не найдена.
    echo Скачайте https://github.com/electron/electron/releases ^(electron-vXX.X-win32-x64.zip^)
    echo и распакуйте её в папку AudioSplitter, затем переименуйте electron.exe в AudioSplitter.exe.
    pause
    exit /b 1
)
if exist "AudioSplitter\resources\app.asar" del "AudioSplitter\resources\app.asar"
if exist "AudioSplitter\resources\app" rmdir /s /q "AudioSplitter\resources\app"
mkdir "AudioSplitter\resources\app"
copy /y "main.js" "AudioSplitter\resources\app\main.js" >nul
copy /y "package.json" "AudioSplitter\resources\app\package.json" >nul
copy /y "..\AudioSplitter_HTML\AudioSplitter.html" "AudioSplitter\resources\app\AudioSplitter.html" >nul
xcopy "..\AudioSplitter_HTML\library" "AudioSplitter\resources\app\library" /e /i /y >nul
echo Готово: запускайте AudioSplitter\AudioSplitter.exe
pause
