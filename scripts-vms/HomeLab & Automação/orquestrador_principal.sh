---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "homelab___automa__o"
protocolo: "ARC"
---

#!/bin/bash
# PASTA: HomeLab-Automacao
# NOME: orquestrador_principal.sh
# FUNÇÃO: Orquestra a execução da infraestrutura do ACVM em ordem de dependência.
# REQUISITOS: Bash shell, permissões de execução (chmod +x)

# Caminhos
LOG_FILE="/var/log/acvm_orquestrador.log"
SCRIPTS_DIR="C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vm's"

# Ordem de execução: Infraestrutura -> Monitoramento -> Serviços -> Notificações e Webhooks -> Utilitários -> HomeLab & Automação

# Adicione ou remova categorias conforme sua estrutura de pastas
ORDEM_CATEGORIAS=("Rede" "Monitoramento" "Seguranca" "Servicos" "Notificações e Webhooks" "Utilitários" "HomeLab & Automação")

echo "[$(date)] --- INICIANDO ORQUESTRAÇÃO ACVM ---" >> $LOG_FILE

for categoria in "${ORDEM_CATEGORIAS[@]}"; do
    PASTA_CAT="$SCRIPTS_DIR/$categoria"
    
    if [ -d "$PASTA_CAT" ]; then
        echo "[$(date)] Processando categoria: $categoria" >> $LOG_FILE
        
        for script in "$PASTA_CAT"/*.sh; do
            # Ignora o próprio orquestrador se ele estiver nesta pasta
            if [[ "$script" == *"orquestrador_principal.sh"* ]]; then continue; fi
            
            if [ -x "$script" ]; then
                echo "   -> Executando: $script" >> $LOG_FILE
                bash "$script"
                
                if [ $? -ne 0 ]; then
                    echo "   [!] ERRO no script: $script" >> $LOG_FILE
                    # Decida se o orquestrador para ou continua em caso de erro
                fi
            fi
        done
    else
        echo "[!] Categoria não encontrada: $categoria" >> $LOG_FILE
    fi
done

echo "[$(date)] --- ORQUESTRAÇÃO CONCLUÍDA ---" >> $LOG_FILE
