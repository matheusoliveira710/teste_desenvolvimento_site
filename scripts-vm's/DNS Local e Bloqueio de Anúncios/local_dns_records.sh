#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi
echo "📝 Adicionando registro DNS local no /etc/hosts..."
echo "Digite o IP do serviço (ex: 192.168.1.150):"
read -r SERVICE_IP
echo "Digite o domínio local desejado (ex: portainer.lab):"
read -r SERVICE_DOMAIN

if grep -q "$SERVICE_DOMAIN" /etc/hosts; then
    sed -i "s/.*$SERVICE_DOMAIN/$SERVICE_IP\t$SERVICE_DOMAIN/g" /etc/hosts
else
    echo -e "$SERVICE_IP\t$SERVICE_DOMAIN" >> /etc/hosts
fi
echo "✅ Apontamento criado: $SERVICE_DOMAIN -> $SERVICE_IP"