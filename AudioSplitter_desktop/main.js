// AudioSplitter — десктопная обёртка (Electron).
// Приложение живёт рядом (AudioSplitter.html + library/), окно — Chromium без адресной строки.
const { app, BrowserWindow, session } = require('electron');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 1400,
        height: 920,
        minWidth: 900,
        minHeight: 600,
        backgroundColor: '#070b16',
        title: 'AudioSplitter',
        autoHideMenuBar: true,
        webPreferences: {
            contextIsolation: true,
            nodeIntegration: false,
            spellcheck: false,
        },
    });
    win.setMenu(null);
    win.loadFile(path.join(__dirname, 'AudioSplitter.html'));
}

app.whenReady().then(() => {
    // локальное доверенное приложение: микрофон и доступ к папке библиотеки разрешаем без вопросов
    session.defaultSession.setPermissionRequestHandler((wc, permission, callback) => callback(true));
    session.defaultSession.setPermissionCheckHandler((wc, permission) => true);
    createWindow();
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', () => app.quit());
