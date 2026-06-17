#!/bin/bash
# backup_config_scripts.sh

BACKUP_DIR="/mnt/storage/backups/infra"
mkdir -p "$BACKUP_DIR"
DATA=$(date +%Y-%m-%d_%H-%M)

echo "📦 Compactando repositório de scripts e configurações do sistema..."

# Faz o backup da sua pasta de scripts inteira e do Netplan/Fstab
tar -czf "$BACKUP_DIR/infra_backup_$DATA.tar.gz" \
    "$HOME/scripts-vm's" \
    /etc/netplan/ \
    /etc/fstab \
    2>/dev/null

# Mantém apenas os backups dos últimos 14 dias
find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +14 -delete

echo "✅ Cópia de segurança da infraestrutura salva em: infra_backup_$DATA.tar.gz"