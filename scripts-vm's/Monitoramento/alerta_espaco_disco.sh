#!/bin/bash
# alerta_espaco_disco.sh

# Define o limite percentual máximo
LIMITE=85
USO_ATUAL=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$USO_ATUAL" -gt "$LIMITE" ]; then
    MENSAGEM="🚨 **[ALERTA DE HARDWARE]** O armazenamento principal do servidor está quase cheio! \n• Uso Atual: \`$USO_ATUAL%\` \n• Espaço Livre: \`$(df -h / | awk 'NR==2 {print $4}')\`"
    
    # Chama o seu script centralizador de notificações
    PATH_NOTIFICADOR="$HOME/scripts-vm's/Notificações e Webhooks/notificar_status.sh"
    if [ -f "$PATH_NOTIFICADOR" ]; then
        bash "$PATH_NOTIFICADOR" "$MENSAGEM"
    else
        echo "Aviso: Notificador central não encontrado no caminho esperado."
    fi
fi
