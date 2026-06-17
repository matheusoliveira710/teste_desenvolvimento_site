#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi

echo "🔋 Impedindo suspensão do sistema (Tampa do notebook/Inatividade)..."
if [ -f /etc/systemd/logind.conf ]; then
    sed -i 's/#HandleLidSwitch=suspend/HandleLidSwitch=ignore/g' /etc/systemd/logind.conf
    sed -i 's/#LidSwitchIgnoreInhibited=yes/LidSwitchIgnoreInhibited=no/g' /etc/systemd/logind.conf
    systemctl restart systemd-logind
fi

echo "🌡️ Instalando ferramentas de monitoramento de Hardware..."
apt update && apt install -y lm-sensors htop net-tools Smartmontools
sensors-detect --auto > /dev/null

echo "✅ Ajustes de hardware aplicados!"