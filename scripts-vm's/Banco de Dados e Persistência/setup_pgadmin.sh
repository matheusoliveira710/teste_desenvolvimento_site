#!/bin/bash
echo "📊 Subindo pgAdmin 4 via Docker..."
docker run -d \
  --name pgadmin \
  -p 5050:80 \
  -e 'PGADMIN_DEFAULT_EMAIL=admin@lab.local' \
  -e 'PGADMIN_DEFAULT_PASSWORD=admin' \
  --restart always \
  dpage/pgadmin4
if command -v ufw &> /dev/null; then sudo ufw allow 5050/tcp; sudo ufw reload; fi
echo "✅ pgAdmin pronto em http://localhost:5050 (Email: admin@lab.local / Senha: admin)"