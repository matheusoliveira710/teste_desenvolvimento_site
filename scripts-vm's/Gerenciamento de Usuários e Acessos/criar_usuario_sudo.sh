#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi
echo "👤 Criando novo usuário administrativo..."
echo "Digite o nome do usuário:"
read -r USERNAME
echo "Digite a senha do usuário:"
read -r PASSWORD

useradd -m -s /bin/bash "$USERNAME"
echo "$USERNAME:$PASSWORD" | chpasswd
usermod -aG sudo "$USERNAME"

# Adiciona regra para o sudo não pedir senha para este usuário específico (opcional)
echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > "/etc/sudoers.d/$USERNAME"
chmod 0440 "/etc/sudoers.d/$USERNAME"

echo "✅ Usuário $USERNAME criado com privilégios sudo desimpedidos!"