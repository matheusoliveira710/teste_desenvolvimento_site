---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "monitoramento"
protocolo: "ARC"
---

#!/bin/bash
# Uso: ./alertas-discord.sh "Mensagem de teste"
URL_DISCORD="SEU_WEBHOOK_DO_DISCORD_AQUI"
if [ -z "$1" ] || [ "$URL_DISCORD" == "SEU_WEBHOOK_DO_DISCORD_AQUI" ]; then
    echo "Erro: Defina a mensagem e configure a URL do Webhook no script."
    exit 1
fi
TEXTO=$1
HOSTNAME=$(hostname)
curl -H "Content-Type: application/json" \
     -X POST \
     -d "{\"content\": \"⚠️ **[Alerta - $HOSTNAME]**: $TEXTO\"}" \
     "$URL_DISCORD"