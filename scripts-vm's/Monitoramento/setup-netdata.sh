#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi
echo "📊 Instalando Netdata Monitor (Painel em tempo real)..."
wget -O /tmp/netdata-kickstart.sh https://get.netdata.cloud/kickstart.sh && sh /tmp/netdata-kickstart.sh --non-interactive
if command -v ufw &> /dev/null; then ufw allow 19999/tcp; ufw reload; fi
echo "✅ Netdata pronto na porta http://localhost:19999"
