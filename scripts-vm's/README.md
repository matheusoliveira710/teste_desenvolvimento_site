# 🚀 DevOps & SysAdmin Automation Framework (scripts-vm's)

Este repositório centraliza um framework completo de **Infraestrutura como Código (IaC)** e automação para provisionamento, segurança, monitoramento e manutenção de servidores Linux físicos ou ambientes virtualizados. 

O projeto foi totalmente modularizado em pastas temáticas para garantir manutenibilidade, permitindo o deploy de módulos específicos ou a orquestração completa através de um script mestre.

---

## 📂 Estrutura do Repositório

```text
scripts-vm's/
├── .github/workflows/
│   └── linter.yml                  # CI/CD: Validação automatizada de sintaxe Bash
├── .gitignore                      # Proteção contra vazamento de chaves e segredos
├── LICENSE                         # Licença MIT Permissiva
├── README.md                       # Documentação principal do ecossistema
├── config.env.example              # Template para centralização de variáveis e IPs
├── configurar_tudo.sh              # Orquestrador Mestre do ecossistema
│
├── Ajustes Físicos/
│   └── hardware_energy.sh          # Otimização de energia e suspensão para hardware real
├── Ambientes de Desenvolvimento/
│   ├── instalar_docker_completo.sh # Setup do Docker Engine + Portainer CE
│   ├── subir_bancos_teste.sh       # Provisionamento rápido de instâncias de bancos (Postgres/MySQL/Redis)
│   └── derrubar_ambiente_teste.sh  # Destruição e liberação de RAM de ambientes temporários
├── Alta Disponibilidade/
│   ├── setup_docker_swarm.sh       # Criação rápida de clusters nativos do Docker
│   └── setup_k3s_master.sh         # Instalação simplificada de nós Kubernetes (K3s)
├── Automations e CI-CD/
│   ├── setup_ansible.sh            # Instalação do gerenciador de configuração Ansible
│   └── setup_github_runner.sh      # Vinculação de Self-Hosted Runners para deploys automáticos
├── Banco de Dados e Persistência/
│   ├── deploy_postgres_cluster.sh  # Cluster PostgreSQL oficial com volumes persistentes
│   └── setup_pgadmin.sh            # Interface web para administração de bancos de dados
├── Customização Estética/
│   ├── cockpit-panel.sh            # Dashboard web oficial para gerenciamento do SO
│   └── Customização-do-Terminal-SSH.sh # Customização do MOTD dinâmico de boas-vindas do SSH
├── Discos/
│   └── ssd_hd.sh                   # Particionamento e montagem definitiva no /etc/fstab
├── DNS Local e AdBlock/
│   ├── deploy_pihole_adblock.sh    # Docker Pi-hole para bloqueio de anúncios via DNS na rede local
│   └── local_dns_records.sh        # Injeção de registros locais no resolvedor do host
├── Gerenciamento de Usuários/
│   ├── criar_usuario_sudo.sh       # Criação padronizada de usuários com privilégios administrativos
│   └── importar_chaves_ssh.sh      # Importação dinâmica de chaves públicas via API do GitHub
├── Limpeza Automática/
│   └── limpeza.sh                  # Faxina de caches (APT), logs (Journald) e lixo de containers
├── Logs e Diagnósticos/
│   ├── check_hardware_health.sh    # Auditoria de S.M.A.R.T nos discos e telemetria térmica
│   └── docker_logs_tail.sh         # Agrupamento e leitura em tempo real de logs críticos
├── Media e Home Server/
│   ├── setup_jellyfin.sh           # Servidor de streaming de mídia local via container
│   └── setup_samba_share.sh        # Compartilhamento de arquivos em rede nativa (NAS)
├── Monitoramento/
│   ├── setup-netdata.sh            # Telemetria em tempo real e gráficos via Web
│   └── alerta_espaco_disco.sh      # Gatilho de segurança contra estouro de armazenamento
├── Notificações e Webhooks/
│   ├── alerta_login_ssh.sh         # Hook no PAM para disparar notificações em acessos remotos
│   └── notificar_status.sh         # Centralizador agnóstico de envio de webhooks (Discord/Telegram)
├── Rede/
│   ├── config_rede.sh              # Configuração definitiva de IP Estático e DNS via Netplan
│   └── configurar_ufw.sh           # Hardening do host através de regras estritas de Firewall (UFW)
├── Redirecionamento e Proxy/
│   └── setup-nginx-proxy-manager.sh # Proxy reverso gráfico com gerenciamento de SSL automático
├── Segurança Dados/
│   ├── backup-cron.sh              # Agendamento automatizado de diretórios do host
│   ├── backup_banco_dados.sh       # Dump de segurança compactado e rotacionado do PostgreSQL
│   └── backup_config_scripts.sh    # Backup de segurança da própria infraestrutura e scripts
├── Segredos e Criptografia/
│   ├── encrypt_secrets.sh          # Encriptação simétrica AES-256 de variáveis locais via GPG
│   └── decrypt_secrets.sh          # Decodificação de arquivos sensíveis pré-deploy
└── Testes e Validação/
    ├── validate_all_syntax.sh      # Varredura estática de integridade via ShellCheck local
    └── mock_deploy.sh              # Simulação Dry-Run de orquestração do ecossistema