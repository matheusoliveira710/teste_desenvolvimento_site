---
tipo: hub
---

TABLE WITHOUT ID 
    file.link AS "Script", 
    status AS "Status", 
    categoria AS "Categoria", 
    protocolo AS "Protocolo",
    file.folder AS "Pasta", 
    file.mday AS "Modificado"
FROM "scripts-vms"
WHERE status != null
SORT file.mday DESC


## Índice Central de Operações

[[ancorar_hub.py]]
[[limpador_grafo.py]]
[[migrador_arc.py]]
[[padronizador_vm.py]]
[[reintegrador_orbital.py]]
[[reintegrar_arc.py]]
[[remover_indice.py]]

## Índice de Infraestrutura e Projetos
- [[hardware_energy]]
- [[derrubar_ambiente_teste]]
- [[instalar_docker_completo]]
- [[setup_node_env]]
- [[subir_bancos_teste]]
- [[setup_ansible]]
- [[setup_github_runner]]
- [[deploy_postgres_cluster]]
- [[setup_pgadmin]]
- [[check_user_privileges]]
- [[log_package_updates]]
- [[cockpit-panel]]
- [[Customização-do-Terminal-SSH]]
- [[setup_python_venv]]
- [[ssh_alias_generator]]
- [[ssd_hd]]
- [[deploy_pihole_adblock]]
- [[local_dns_records]]
- [[criar_usuario_sudo]]
- [[importar_chaves_ssh]]
- [[download_git_release]]
- [[scan_rede_local]]
- [[notificar]]
- [[orquestrador_principal]]
- [[weather_alert_cron]]
- [[limpeza]]
- [[alertas-discord]]
- [[alerta_espaco_disco]]
- [[check_saude_disco]]
- [[monitorar_conectividade]]
- [[setup-netdata]]
- [[status_manha]]
- [[alerta_login_ssh]]
- [[notificar_status]]
- [[notify_task_finished]]
- [[configurar_ufw]]
- [[config_rede]]
- [[show_active_connections]]
- [[speedtest_logger]]
- [[tailscale-vpn]]
- [[setup-nginx-proxy-manager]]
- [[weather_motd]]
- [[gerar_par_chaves_ssh]]
- [[backup-cron]]
- [[backup_config_scripts]]
- [[relatorio_de_acessos]]
- [[monitor_sudo_activity]]
- [[reiniciar_servicos_travados]]
- [[auto_update_system]]
- [[backup_banco_dados]]
- [[check_temp_cpu]]
- [[get_weather_forecast]]
- [[setar_hostname]]
- [[teste_velocidade]]
- [[weather_dashboard_cli]]
- [[weather_forecast]]