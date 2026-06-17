#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi
echo "🤖 Instalando Ansible Core..."
apt update && apt install -y software-properties-common
add-apt-repository --yes --update ppa:ansible/ansible
apt install -y ansible
echo "✅ Ansible instalado! Versão: $(ansible --version | head -n 1)"