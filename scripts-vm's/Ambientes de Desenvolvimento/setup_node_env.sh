#!/bin/bash
echo "🚀 Instalando NVM e Node.js LTS..."

# Instala o NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Carrega o NVM para a sessão atual
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Instala a versão LTS mais recente
nvm install --lts
nvm use --lts

echo "✅ Node.js $(node -v) e NPM $(npm -v) instalados com sucesso!"
