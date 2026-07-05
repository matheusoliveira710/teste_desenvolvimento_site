---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "customiza__o_est_tica"
protocolo: "ARC"
---

#!/bin/bash
# 10-cockpit-panel.sh
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi

echo "📊 Instalando Cockpit Dashboard..."
apt update && apt install -y cockpit

systemctl enable cockpit.socket --now

if command -v ufw &> /dev/null; then
    ufw allow 9090/tcp
    ufw reload
fi

echo "🚀 Cockpit pronto! Acesse no seu navegador: https://$(hostname -I | awk '{print $1}'):9090"
