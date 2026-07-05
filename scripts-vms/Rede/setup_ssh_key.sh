#!/bin/bash
# Objetivo: Configurar SSH Keyless no ACVM

REMOTE_USER="matheus"
REMOTE_HOST="acvm-server" # Certifique-se de ter definido o IP no seu /etc/hosts
KEY_PATH="$HOME/.ssh/id_rsa"

echo "--- Iniciando configuração SSH ---"

# Gera a chave se não existir
if [ ! -f "$KEY_PATH" ]; then
    ssh-keygen -t rsa -b 4096 -f "$KEY_PATH" -N ""
fi

# Copia a chave com segurança
ssh-copy-id -i "$KEY_PATH.pub" $REMOTE_USER@$REMOTE_HOST

if [ $? -eq 0 ]; then
    echo "[+] Sucesso! Agora você acessa o ACVM sem senha."
    ./notify_task_finished.sh "sucesso" "SSH Key configurada no ACVM"
else
    echo "[!] Falha na configuração SSH."
    ./notify_task_finished.sh "erro" "Falha ao configurar SSH no ACVM"
    exit 1
fi
