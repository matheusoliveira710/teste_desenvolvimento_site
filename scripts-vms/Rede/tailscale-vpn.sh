#!/bin/bash
# ---
# dashboard: [[Dashboard_ACVM]]
# status: "Operacional"
# categoria: "rede"
# protocolo: "ARC"
# ---

# Removemos a verificação de EUID pois o Windows gerencia permissões de outra forma
echo "🌐 Iniciando gerenciamento Tailscale..."

# Se estiver no Windows, usa winget. Se estiver em Linux/WSL, usa o comando original.
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    echo "💡 Detectado Windows. Certifique-se de que o Tailscale já esteja instalado."
    echo "Comando: tailscale up"
    # Se o Tailscale estiver no PATH do Windows, este comando funcionará
    tailscale up
else
    # Lógica original para sistemas baseados em Unix
    if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi
    tailscale up
fi