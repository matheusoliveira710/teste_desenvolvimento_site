#!/bin/bash
if [ "$EUID" -ne 0 ]; then echo "Rode como sudo"; exit 1; fi
echo "🔔 Configurando gatilho de alerta para logins SSH..."

# Cria o script que será disparado pelo PAM quando alguém logar
cat << 'EOF' > /usr/local/bin/ssh_alert_trigger.sh
#!/bin/bash
# Não disparar se for o carregamento comum do sistema
if [ "$PAM_TYPE" = "open_session" ]; then
    MENSAJE="👤 **Login SSH detectado!**\n• Usuário: \`$PAM_USER\`\n• IP de Origem: \`$PAM_RHOST\`\n• Host: \`$(hostname)\`"
    # Chama o script centralizador de notificações
    /home/$PAM_USER/scripts-vm's/Notificações\ e\ Webhooks/notificar_status.sh "$MENSAJE"
fi
EOF

chmod +x /usr/local/bin/ssh_alert_trigger.sh

# Adiciona o gancho no PAM do SSH
if ! grep -q "ssh_alert_trigger.sh" /etc/pam.d/sshd; then
    echo "session optional pam_exec.so /usr/local/bin/ssh_alert_trigger.sh" >> /etc/pam.d/sshd
fi
echo "✅ Monitoramento de logins SSH ativado com sucesso!"