#!/bin/bash
# weather_motd.sh - Exibe clima e status do sistema no login

# 1. Busca previsão do tempo para Campinas (sem necessidade de chave de API)
# O wttr.in é um serviço excelente para terminais
CLIMA=$(curl -s "wttr.in/Campinas?format=3")

# 2. Coleta status básico do servidor
UPTIME=$(uptime -p | sed 's/up //')
LOAD=$(cat /proc/loadavg | awk '{print $1, $2, $3}')
MEM_USO=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2}')
TEMP=$(cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null | awk '{print $1/1000 "°C"}')

# Define as cores
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${CYAN}===================================================="
echo -e "  Bem-vindo, Matheus!"
echo -e "  Status do Servidor: ${GREEN}$(hostname)${NC}"
echo -e "${CYAN}===================================================="
echo -e "${YELLOW}🌤️  Clima em Campinas:${NC} $CLIMA"
echo -e "${YELLOW}⏱️  Tempo ativo:${NC} $UPTIME"
echo -e "${YELLOW}📊 Carga (Load Avg):${NC} $LOAD"
echo -e "${YELLOW}🧠 Uso de RAM:${NC} $MEM_USO"
[ -n "$TEMP" ] && echo -e "${YELLOW}🔥 Temp CPU:${NC} $TEMP"
echo -e "${CYAN}====================================================${NC}"