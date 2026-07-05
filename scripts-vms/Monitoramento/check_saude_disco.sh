---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "monitoramento"
protocolo: "ARC"
---

#!/bin/bash
# PASTA: Monitoramento
# NOME: check_saude_disco.sh
# FUNÇÃO: Realiza diagnóstico de saúde do hardware via S.M.A.R.T.
# UTILIZADO POR: orquestrador_principal.sh

# Altere /dev/sda se o seu disco principal tiver outro identificador
DISK="/dev/sda"
LOG_FILE="/var/log/acvm_hardware.log"

echo "[$(date)] Iniciando diagnóstico S.M.A.R.T. em $DISK..." >> $LOG_FILE

# Verifica se o smartmontools está instalado
if ! command -v smartctl &> /dev/null; then
    echo "ERRO: smartmontools não está instalado. Rode 'sudo apt install smartmontools'." >> $LOG_FILE
    exit 1
fi

# Executa o diagnóstico rápido de saúde
SAUDE=$(sudo smartctl -H $DISK | grep "result" | awk '{print $6}')

if [ "$SAUDE" == "PASSED" ]; then
    echo "STATUS: Disco Saudável." >> $LOG_FILE
    exit 0
else
    echo "ALERTA: Falha iminente no disco! Status retornado: $SAUDE" >> $LOG_FILE
    exit 1
fi