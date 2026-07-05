---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "customiza__o_est_tica"
protocolo: "ARC"
---

#!/bin/bash
# 09-banner-motd.sh
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi

echo "🎨 Personalizando tela de boas-vindas do SSH..."
# Desativa avisos padrões chatos
chmod -x /etc/update-motd.d/* 2>/dev/null

# Cria nosso layout customizado dinâmico
cat << 'EOF' > /etc/update-motd.d/99-custom
#!/bin/bash
CLEAR='\033[0m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'

echo -e "${BLUE}"
echo "  ======================================================="
echo "     BEM-VINDO AO SEU SERVIDOR DOMÉSTICO (HOMELAB)     "
echo "  ======================================================="
echo -e "${CLEAR}"
echo -e "  Uptime do Sistema : $(uptime -p)"
echo -e "  Memória RAM livre : $(free -h | awk '/^Mem:/ {print $4 " de " $2}')"
echo -e "  Uso do Espaço /   : $(df -h / | awk 'NR==2 {print $5 " ocupado (" $4 " disponível)"}')"
echo -e "  IP Local          : $(hostname -I | awk '{print $1}')"
echo -e "${BLUE}  =======================================================${CLEAR}"
EOF

chmod +x /etc/update-motd.d/99-custom
echo "✅ Terminal personalizado! Desconecte e conecte via SSH de novo para ver."
