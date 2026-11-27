# AudioSplitter — десктопная версия (Windows)

`AudioSplitter.exe` запускает приложение в отдельном окне: без браузера и адресной строки.
Работают все функции: волна, фрагменты, дорожки, 🧠 Нейро, запись с микрофона, библиотека.

## Запуск

`AudioSplitter\AudioSplitter.exe` — двойной щелчок.

## Как устроено

- Рантайм Electron распакован в папку `AudioSplitter\` (exe + Chromium).
- Само приложение лежит в `AudioSplitter\resources\app\` — там `AudioSplitter.html`, `library\` и обёртка `main.js`.
- Микрофон и доступ к папке библиотеки разрешены обёрткой без диалогов (локальное доверенное приложение).

## Обновление приложения внутри exe

После правок HTML-версии запустите `build-desktop.bat` — он скопирует свежие
`AudioSplitter.html` и `library\` из `AudioSplitter_HTML\` в `resources\app`.

## Если папки AudioSplitter нет (клон репо с нуля)

1. Скачайте `electron-vXX.X-win32-x64.zip` со страницы релизов Electron:
   https://github.com/electron/electron/releases
2. Распакуйте архив в папку `AudioSplitter\` этого каталога.
3. Переименуйте `electron.exe` в `AudioSplitter.exe`.
4. Запустите `build-desktop.bat`.
