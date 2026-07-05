---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "rede"
protocolo: "ARC"
---

#!/bin/bash

Requer: apt install speedtest-cli

sudo apt install speedtest-cli

echo”Instalando pacote SpeedTest”

echo "Executando teste de velocidade..."
speedtest-cli --simple >> ~/speedtest_log.txt
echo "Resultado registrado em ~/speedtest_log.txt"