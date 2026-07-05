---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "notifica__es_e_webhooks"
protocolo: "ARC"
---

#!/bin/bash
# Uso: ./notify_task_finished.sh "Mensagem aqui"
MENSAGEM=${1:-"Tarefa finalizada com sucesso!"}
HOSTNAME=$(hostname)

# Define o caminho do seu notificador central
NOTIFICADOR="$HOME/scripts-vm's/Notificações e Webhooks/notificar_status.sh"

if [ -f "$NOTIFICADOR" ]; then
    bash "$NOTIFICADOR" "✅ **[$HOSTNAME]** $MENSAGEM"
else
    echo "Erro: Notificador central não encontrado."
fi
