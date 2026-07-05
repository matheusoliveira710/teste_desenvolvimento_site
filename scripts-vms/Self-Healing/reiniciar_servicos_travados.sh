---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "self_healing"
protocolo: "ARC"
---

#!/bin/bash
# reiniciar_servicos_travados.sh - Auto-cura de serviços críticos

# Lista de serviços para monitorar
SERVICOS=("ssh" "docker" "nginx")
NOTIFICADOR="$HOME/scripts-vm's/Notificações e Webhooks/notificar_status.sh"

echo "🩺 Verificando saúde dos serviços..."

for servico in "${SERVICOS[@]}"; do
    if ! systemctl is-active --quiet "$servico"; then
        echo -e "⚠️ Serviço \e[31m$servico\e[0m está parado. Tentando reiniciar..."
        
        systemctl restart "$servico"
        
        sleep 2
        
        if systemctl is-active --quiet "$servico"; then
            MSG="✅ **[Auto-cura]**: O serviço \`$servico\` estava parado e foi reiniciado com sucesso!"
            echo "$MSG"
            [ -f "$NOTIFICADOR" ] && bash "$NOTIFICADOR" "$MSG"
        else
            MSG="🚨 **[ALERTA CRÍTICO]**: O serviço \`$servico\` não respondeu ao comando de reinicialização!"
            echo "$MSG"
            [ -f "$NOTIFICADOR" ] && bash "$NOTIFICADOR" "$MSG"
        fi
    else
        echo -e "✅ Serviço \e[32m$servico\e[0m está operante."
    fi
done
