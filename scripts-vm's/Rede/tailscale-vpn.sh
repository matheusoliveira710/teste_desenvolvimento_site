#!/bin/bash
# 07-tailscale-vpn.sh
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi

echo "🌐 Instalar Tailscale VPN..."
curl -fsSL https://tailscale.com/install.sh | sh

echo "🚀 Iniciando Tailscale..."
tailscale up

echo "🔗 Copie o link acima para autorizar este servidor na sua conta Tailscale!"
