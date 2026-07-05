---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "discos"
protocolo: "ARC"
---

#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi

echo "💾 Discos detectados no sistema:"
lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS | grep -v "loop"
echo "----------------------------------------"
echo "Digite o identificador do disco que quer montar (ex: sdb1 ou nvme1n1p1):"
read -r DISK

if [ ! -b "/dev/$DISK" ]; then
    echo "Disco inválido!"
    exit 1
fi

echo "Digite o nome da pasta de destino em /mnt/ (ex: storage ou hd_externo):"
read -r FOLDER

UUID=$(blkid -s UUID -o value "/dev/$DISK")
MOUNT_POINT="/mnt/$FOLDER"

mkdir -p "$MOUNT_POINT"

# Adiciona no fstab para ser definitivo
if ! grep -q "$UUID" /etc/fstab; then
    echo "UUID=$UUID $MOUNT_POINT ext4 defaults 0 2" >> /etc/fstab
    mount -a
    echo "💾 Disco /dev/$DISK montado em $MOUNT_POINT com sucesso!"
else
    echo "⚠️ Este disco já está configurado no /etc/fstab."
fi
