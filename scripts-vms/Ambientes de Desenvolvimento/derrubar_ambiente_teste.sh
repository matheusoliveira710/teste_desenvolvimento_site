---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "ambientes_de_desenvolvimento"
protocolo: "ARC"
---

#!/bin/bash

# Cores para o terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}=====================================================${NC}"
echo -e "${BLUE}       ENCERRANDO AMBIENTES DE TESTE LOCAIS          ${NC}"
echo -e "${BLUE}=====================================================${NC}"

# Lista dos containers criados no script de subida
CONTAINERS=("pg-test" "mysql-test" "redis-test")
REMOVIDOS=0

for container in "${CONTAINERS[@]}"; do
    # Verifica se o container existe (rodando ou parado)
    if docker ps -a --format '{{.Names}}' | grep -Eq "^${container}$"; then
        echo -e "${YELLOW}Parando e removendo o container: $container...${NC}"
        # Força a parada e remoção do container de forma limpa
        docker rm -f "$container" > /dev/null 2>&1
        echo -e "${GREEN}✓ $container removido.${NC}"
        REMOVIDOS=$((REMOVIDOS + 1))
    else
        echo -e "${NC}○ $container não encontrado ou já foi removido.${NC}"
    fi
done

echo -e "${BLUE}=====================================================${NC}"
if [ "$REMOVIDOS" -gt 0 ]; then
    echo -e "${GREEN}✅ Sucesso! $REMOVIDOS ambiente(s) limpo(s) e RAM liberada!${NC}"
else
    echo -e "${YELLOW}Nenhum container de teste ativo precisou ser removido.${NC}"
fi
echo -e "${BLUE}=====================================================${NC}"