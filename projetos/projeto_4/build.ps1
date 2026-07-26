Write-Host "==> Iniciando a build do Matriz Eisenhower..." -ForegroundColor Cyan
pyinstaller --noconsole --onefile app.py
Write-Host "==> Build concluida! O executavel esta na pasta 'dist/'." -ForegroundColor Green
Read-Host "Pressione Enter para sair"