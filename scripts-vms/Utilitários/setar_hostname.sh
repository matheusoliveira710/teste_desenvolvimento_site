---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "utilit_rios"
protocolo: "ARC"
---

#!/bin/bash

# Script para definir o hostname do sistema
# Uso: sudo ./setar_hostname.sh "novo-nome"

NOVO_HOSTNAME=$1

if [ -z "$NOVO_HOSTNAME" ]; then
    echo "Erro: Você precisa informar o novo hostname."
    echo "Exemplo: sudo ./setar_hostname.sh servidor-lab-01"
    exit 1
fi

echo "Alterando hostname para: $NOVO_HOSTNAME"

# 1. Altera no /etc/hostname
echo "$NOVO_HOSTNAME" | sudo tee /etc/hostname > /dev/null

# 2. Altera no /etc/hosts para evitar erros de resolução local
sudo sed -i "s/127.0.1.1.*/127.0.1.1\t$NOVO_HOSTNAME/g" /etc/hosts

# 3. Aplica o comando hostnamectl para surtir efeito imediato
sudo hostnamectl set-hostname "$NOVO_HOSTNAME"

echo "Hostname alterado com sucesso para $(hostname)!"
echo "Recomenda-se abrir um novo terminal para ver a alteração no prompt."
