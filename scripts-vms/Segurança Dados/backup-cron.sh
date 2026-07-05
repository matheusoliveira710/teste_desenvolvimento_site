---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "seguran_a_dados"
protocolo: "ARC"
---

#!/bin/bash
# 06-backup-cron.sh

BACKUP_DIR="/mnt/storage/backups"
SOURCE_DIR="/var/lib/docker/volumes" # Exemplo: volumes do docker

mkdir -p "$BACKUP_DIR"

# Script interno que o cron vai executar
cat << 'EOF' > /usr/local/bin/deity_backup.sh
#!/bin/bash
BACKUP_DIR="/mnt/storage/backups"
SOURCE_DIR="/var/lib/docker/volumes"
DATA=$(date +%Y-%m-%d_%H-%M-%s)

tar -czf "$BACKUP_DIR/backup_docker_$DATA.tar.gz" "$SOURCE_DIR" 2>/dev/null

# Remove arquivos com mais de 7 dias
find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +7 -delete
EOF

chmod +x /usr/local/bin/deity_backup.sh

# Adiciona no crontab para rodar todo dia às 3h da manhã
(crontab -l 2>/dev/null; echo "0 3 * * * /usr/local/bin/deity_backup.sh") | crontab -
echo "⏰ Rotina de backup agendada para as 03:00 diariamente!"
