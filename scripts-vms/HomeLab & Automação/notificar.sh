---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "automacao"
protocolo: "ARC"
---

# ==============================================================================
# SCRIPT: notificar.sh
# FUNÇÃO: Centraliza envios de mensagens para os canais do Discord via Webhooks.
# DIRETÓRIO: Utilitários
# STATUS: Operacional
# ==============================================================================

# --- CONFIGURAÇÃO DE WEBHOOKS ---
URL_ALERTA_PRIO="https://discord.com/api/webhooks/1519711446445981805/RMb3waFX8JoRFwpgmg32ga5SasqgQsNa7C6J1RcuxU6Ag9Z-fBK2TS_8kl5IxkOPoC70"
URL_STORAGE_HEALTH="https://discord.com/api/webhooks/1519709329215721483/gXSWP-sBX57iHskFtdTBu877nBf6dT4v7uQW3dijVlsK8QXgafRF66jbFsBYdullvsTJ"
URL_SSH_AUDIT="https://discord.com/api/webhooks/1519711648229625999/RJ56lC-xBtSJ8imeL8Dmz9OYYI_yREu4lhp9RGtw8TupZo0Yv5d8oFjyd9NRgicCRdls"
URL_APT_UPDATES="https://discord.com/api/webhooks/1519711931219447829/iPPUGsd_Fy-Va7JJ0V8936Zb5UgLNiFAAkvFTXG-o9uPvzQJDq-Gm_OBq0yybQG7jo0w"
URL_CRON_STATUS="https://discord.com/api/webhooks/1519712074932949122/jBM-l3EHn8Ax3eMCXEZ5x7Tg0WlD-dSfinZqZ7ZW6ZRRjkMtD8Gb9IiXmOmz4pnBmVHW"

notificar() {
    local canal=$1
    local mensagem=$2
    local url=""

    case $canal in
        "alerta-prio")   url=$URL_ALERTA_PRIO ;;
        "storage-health") url=$URL_STORAGE_HEALTH ;;
        "ssh-audit")      url=$URL_SSH_AUDIT ;;
        "apt-updates")    url=$URL_APT_UPDATES ;;
        "cron-status")    url=$URL_CRON_STATUS ;;
        *) 
            echo "[!] Erro: Canal '$canal' não mapeado no notificar.sh"
            return 1 
            ;;
    esac

    # Envio da mensagem usando curl
    curl -H "Content-Type: application/json" \
         -X POST \
         -d "{\"content\": \"$mensagem\"}" \
         $url
}

# Permite rodar o script diretamente pelo terminal
if [ "$1" != "" ] && [ "$2" != "" ]; then
    notificar "$1" "$2"
fi