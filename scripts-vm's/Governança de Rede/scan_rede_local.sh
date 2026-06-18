#!/bin/bash
# scan_rede_local.sh - Identifica dispositivos na rede local

if ! command -v nmap &> /dev/null; then
    echo "📦 Instalando nmap..."
    sudo apt update && sudo apt install -y nmap
fi

# Detecta automaticamente a sub-rede (ex: 192.168.1.0/24)
SUBNET=$(ip route | grep default | awk '{print $3}' | cut -d. -f1-3).0/24

echo "🔍 Escaneando a rede: $SUBNET"
echo "--------------------------------------------------------"
# O -sn faz o ping scan (mais rápido)
sudo nmap -sn "$SUBNET" | grep "Nmap scan report for" | awk '{print $5, $6}'
echo "--------------------------------------------------------"
echo "✅ Scan finalizado em: $(date)"
