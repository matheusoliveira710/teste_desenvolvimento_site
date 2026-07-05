---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "monitoramento"
protocolo: "ARC"
---

#!/bin/bash
# PASTA: Monitoramento
# NOME: monitorar_conectividade.sh
# FUNÇÃO: Valida a conectividade com o Gateway e com o DNS externo (Google).
# UTILIZADO POR: orquestrador_principal.sh

LOG_FILE="/var/log/acvm_monitoramento.log"
GATEWAY="192.168.1.1"
DNS_EXTERNO="8.8.8.8"

echo "[$(date)] Iniciando verificação de conectividade..." >> $LOG_FILE

# Teste de Gateway
if ping -c 1 $GATEWAY &> /dev/null; then
    echo "Gateway ($GATEWAY) OK" >> $LOG_FILE
else
    echo "ERRO: Gateway ($GATEWAY) inacessível!" >> $LOG_FILE
    exit 1
fi

# Teste de Internet
if ping -c 1 $DNS_EXTERNO &> /dev/null; then
    echo "Conectividade Externa (DNS) OK" >> $LOG_FILE
else
    echo "ERRO: Sem acesso à internet!" >> $LOG_FILE
    exit 1
fi

echo "[$(date)] Verificação concluída com sucesso." >> $LOG_FILE