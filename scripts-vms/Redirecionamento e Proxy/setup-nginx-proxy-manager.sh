---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "redirecionamento_e_proxy"
protocolo: "ARC"
---

#!/bin/bash
echo "🌐 Subindo Nginx Proxy Manager..."
mkdir -p /mnt/storage/nginx_proxy/data /mnt/storage/nginx_proxy/letsencrypt
docker run -d \
  --name nginx-proxy-manager \
  -p 80:80 -p 81:81 -p 443:443 \
  -v /mnt/storage/nginx_proxy/data:/data \
  -v /mnt/storage/nginx_proxy/letsencrypt:/etc/letsencrypt \
  --restart always \
  jc21/nginx-proxy-manager:latest
if command -v ufw &> /dev/null; then sudo ufw allow 80/tcp; sudo ufw allow 81/tcp; sudo ufw allow 443/tcp; sudo ufw reload; fi
echo "✅ Nginx Proxy Manager pronto! Painel Admin em http://localhost:81 (User: admin@example.com / Pass: changeme)"