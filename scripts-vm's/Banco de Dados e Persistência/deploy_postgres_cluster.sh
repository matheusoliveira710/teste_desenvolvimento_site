#!/bin/bash
echo "🐘 Subindo cluster PostgreSQL com volume persistente..."
mkdir -p /mnt/storage/postgres_data
docker run -d \
  --name postgres-cluster \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=homelab \
  -v /mnt/storage/postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --restart always \
  postgres:16-alpine
if command -v ufw &> /dev/null; then sudo ufw allow 5432/tcp; sudo ufw reload; fi
echo "✅ PostgreSQL ativo na porta 5432!"
