#!/bin/bash
echo "🚀 Levantando bancos de dados rápidos para testes (Docker)..."
docker run -d --name pg-test -e POSTGRES_PASSWORD=postgres -p 5433:5432 --restart unless-stopped postgres:alpine
docker run -d --name mysql-test -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --restart unless-stopped mysql:latest
docker run -d --name redis-test -p 6379:6379 --restart unless-stopped redis:alpine
echo "✅ Bancos ativos locais: Postgres (Porta 5433), MySQL (Porta 3306), Redis (Porta 6379)"