---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "monitoramento"
protocolo: "ARC"
---

#!/bin/bash
# PASTA: Monitoramento
# NOME: status_manha.sh
# FUNÇÃO: Relatório matinal do J.A.R.V.I.S.

NOTIFICADOR="../HomeLab & Automação/notificar.sh" # Ajuste o caminho se necessário

# Coleta de dados básicos
TEMPERATURA=$(sensors | grep "Package id 0" | awk '{print $4}')
UPTIME=$(uptime -p)
USO_DISCO=$(df -h / | grep / | awk '{print $5}')

MENSAGEM="Bom dia, Senhor. O servidor $(hostname) está operante. 
- Status atual: $UPTIME
- Temperatura: $TEMPERATURA
- Uso do disco principal: $USO_DISCO
Todos os sistemas estão dentro dos parâmetros de segurança."

bash "$NOTIFICADOR" "cron-status" "$MENSAGEM"
