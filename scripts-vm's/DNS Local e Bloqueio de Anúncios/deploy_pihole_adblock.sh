#!/bin/bash
echo "🛑 Subindo Pi-hole (Bloqueador de anúncios no DNS)..."
mkdir -p /mnt/storage/pihole /mnt/storage/dnsmasq.d
# Desativa o resolvedor nativo do Ubuntu se ele estiver ocupando a porta 53
systemctl stop systemd-resolved 2>/dev/null
systemctl disable systemd-resolved 2>/dev/null

docker run -d \
  --name pihole \
  -p 53:53/tcp -p 53:53/udp \
  -p 8080:80/tcp \
  -e TZ="America/Sao_Paulo" \
  -e WEBPASSWORD="admin" \
  -v /mnt/storage/pihole:/etc/pihole \
  -v /mnt/storage/dnsmasq.d:/etc/dnsmasq.d \
  --restart always \
  pihole/pihole:latest
if command -v ufw &> /dev/null; then sudo ufw allow 53/tcp; sudo ufw allow 53/udp; sudo ufw allow 8080/tcp; sudo ufw reload; fi
echo "✅ Pi-hole ativo! Painel em http://localhost:8080/admin (Senha: admin)"