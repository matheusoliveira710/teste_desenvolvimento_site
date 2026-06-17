#!/bin/bash
# Uso: sudo ./01-network-ssh.sh <hostname> <ip/cidr> <gateway>
if [ "$EUID" -ne 0 ] || [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
  echo "Uso: sudo $0 <hostname> <ip/cidr> <gateway>"
  exit 1
fi

HOSTNAME=$1; IP=$2; GW=$3
INTERFACE=$(ip -br link show | grep -v "lo" | awk '{print $1}' | head -n 1)

echo "⚙️ Configurando Hostname..."
hostnamectl set-hostname "$HOSTNAME"
sed -i "s/127.0.1.1.*/127.0.1.1\t$HOSTNAME/g" /etc/hosts

echo "🌐 Configurando IP Estático na interface $INTERFACE..."
rm -f /etc/netplan/*.yaml
cat <<EOF > /etc/netplan/00-installer-config.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    $INTERFACE:
      dhcp4: no
      addresses: [$IP]
      routes: [{to: default, via: $GW}]
      nameservers: {addresses: [8.8.8.8, 1.1.1.1]}
EOF
chmod 600 /etc/netplan/00-installer-config.yaml
netplan apply

echo "🔑 Garantindo SSH ativo..."
apt update && apt install -y openssh-server
systemctl enable ssh --now
echo "✅ Configuração de rede e SSH concluída!"
