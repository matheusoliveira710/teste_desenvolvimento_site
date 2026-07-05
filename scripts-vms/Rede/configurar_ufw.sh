---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "rede"
protocolo: "ARC"
---

#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi

echo "🛡️ Configurando Firewall (UFW)..."
apt update && apt install -y ufw fail2ban

# Regras básicas
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp   # SSH
ufw allow 9090/tcp # Cockpit (Se for usar)
ufw allow 9443/tcp # Portainer HTTPS (Se for usar)

ufw --force enable
systemctl enable fail2ban --now
echo "🔒 Firewall Ativo e Fail2Ban monitorando tentativas de invasão!"