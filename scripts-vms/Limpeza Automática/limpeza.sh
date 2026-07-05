---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "limpeza_autom_tica"
protocolo: "ARC"
---

#!/bin/bash

# Cores para o terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Verificar se roda como root
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}Por favor, execute este script como root (sudo).${NC}"
  exit 1
fi

echo -e "${BLUE}=====================================================${NC}"
echo -e "${BLUE}      INICIANDO FAXINA E MANUTENÇÃO DO SISTEMA       ${NC}"
echo -e "${BLUE}=====================================================${NC}"

# 1. Armazenar espaço inicial para comparação
DISK_BEFORE=$(df -h / | awk 'NR==2 {print $4}')
echo -e "${YELLOW}Espaço disponível antes da limpeza: $DISK_BEFORE${NC}\n"

# 2. Limpeza do Gerenciador de Pacotes (APT)
echo -e "${GREEN}[1/4] Limpando cache do APT e pacotes órfãos...${NC}"
# Remove pacotes instalados como dependências que não são mais necessários
apt-get autoremove -y
# Limpa o cache local de arquivos de pacotes baixados (.deb) que já foram instalados
apt-get clean
apt-get autoclean

# 3. Limpeza profunda do Docker (se estiver instalado)
if command -v docker &> /dev/null; then
    echo -e "\n${GREEN}[2/4] Docker detectado! Limpando recursos não utilizados...${NC}"
    # O comando abaixo remove:
    # - Todos os containers parados
    # - Todas as redes não utilizadas
    # - Todas as imagens sem tag/órfãs (dangling images)
    # - Todo o cache de build antigo
    docker system prune -f
    
    # Se quiser uma limpeza ainda mais agressiva (remover TODAS as imagens não usadas por nenhum container ativo):
    # Descomente a linha abaixo retirando a '#'
    # docker system prune -a --volumes -f
else
    echo -e "\n${YELLOW}[2/4] Docker não instalado nesta máquina. Pulando etapa.${NC}"
fi

# 4. Limpeza de Logs antigos do Systemd (Journald)
echo -e "\n${GREEN}[3/4] Compactando e limpando logs do sistema...${NC}"
# Mantém apenas os logs dos últimos 3 dias e apaga o resto
journalctl --vacuum-time=3d

# 5. Limpeza de arquivos temporários antigos
echo -e "\n${GREEN}[4/4] Limpando arquivos temporários obsoletos...${NC}"
find /tmp -type f -atime +2 -delete 2>/dev/null

# =====================================================================
# RESULTADO FINAL
# =====================================================================
DISK_AFTER=$(df -h / | awk 'NR==2 {print $4}')

echo -e "\n${GREEN}=====================================================${NC}"
echo -e "${GREEN}           FAXINA CONCLUÍDA COM SUCESSO!            ${NC}"
echo -e "${GREEN}=====================================================${NC}"
echo -e "${BLUE}Espaço livre ANTES:${NC} $DISK_BEFORE"
echo -e "${BLUE}Espaço livre AGORA:${NC} $DISK_AFTER"
echo -e "${YELLOW}Dica: Você pode agendar este script no seu Crontab para rodar sozinho.${NC}"
echo -e "${GREEN}=====================================================${NC}"
