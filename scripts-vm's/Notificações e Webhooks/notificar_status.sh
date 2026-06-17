#!/bin/bash
# Centralizador de mensageria (Uso genérico: ./notificar_status.sh "texto")
URL_WEBHOOK="SEU_WEBHOOK_DO_DISCORD_OU_TELEGRAM"

if [ -z "$1" ] || [ "$URL_WEBHOOK" == "SEU_WEBHOOK_DO_DISCORD_OU_TELEGRAM" ]; then
    exit 0 # Aborta silenciosamente se não houver mensagem ou webhook configurado
fi

TEXTO=$1

# Se for Discord (contiver discord.com na URL)
if [[ "$URL_WEBHOOK" == *"discord.com"* ]]; then
    curl -H "Content-Type: application/json" -X POST -d "{\"content\": \"$TEXTO\"}" "$URL_WEBHOOK"
fi
