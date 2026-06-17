#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi
echo "🐳 Instalando o ecossistema Docker..."
curl -fsSL https://get.docker.com | sh
if [ -n "$SUDO_USER" ]; then usermod -aG docker "$SUDO_USER"; fi

echo "📊 Instalando Portainer CE..."
docker volume create portainer_data
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest

if command -v ufw &> /dev/null; then ufw allow 9443/tcp; ufw reload; fi
echo "✅ Docker instalado e Portainer rodando em https://localhost:9443"