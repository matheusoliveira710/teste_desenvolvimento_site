#!/bin/bash
# Backup automatizado do container Postgres principal
BACKUP_DIR="/mnt/storage/backups/bancos"
mkdir -p "$BACKUP_DIR"
DATA=$(date +%Y-%m-%d_%H-%M)

if docker ps | grep -q "postgres-cluster"; then
    echo "💾 Executando dump do banco 'homelab'..."
    docker exec -t postgres-cluster pg_dumpall -U postgres > "$BACKUP_DIR/db_backup_$DATA.sql"
    gzip "$BACKUP_DIR/db_backup_$DATA.sql"
    find "$BACKUP_DIR" -type f -name "*.sql.gz" -mtime +7 -delete
    echo "✅ Backup concluído: db_backup_$DATA.sql.gz"
else
    echo "❌ Erro: Container postgres-cluster não está rodando."
fi