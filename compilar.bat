@echo off
echo Iniciando a compilacao do seu app...

:: Remove pastas antigas de compilacao para garantir uma versao limpa
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist app.spec del /f /q app.spec

:: Executa o comando do PyInstaller
pyinstaller --onefile --windowed --hidden-import PyQt5.QtChart app.py

echo.
echo Compilacao finalizada! Verifique a pasta 'dist'.
pause
