#!/bin/bash
# Mostra conexões ativas, o processo dono e o IP de origem
echo "🔍 Conexões de rede ativas (ESTABLISHED):"
echo "--------------------------------------------------------"
ss -tupn | grep ESTAB | awk '{print $1, $5, $6, $7}' | column -t
echo "--------------------------------------------------------"
echo "✅ Lista gerada em: $(date)"
