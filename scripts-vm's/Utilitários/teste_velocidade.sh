#!/bin/bash
echo "⚡ Verificando velocidade da rede do servidor físico..."
if ! command -v speedtest-cli &> /dev/null; then
    sudo apt update && sudo apt install -y speedtest-cli
fi
speedtest-cli --secure