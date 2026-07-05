---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "gerenciamento_de_usu_rios_e_acessos"
protocolo: "ARC"
---

#!/bin/bash
echo "🔑 Importando chaves públicas do GitHub para o authorized_keys..."
echo "Digite o nome do seu usuário do GitHub:"
read -r GH_USER

TARGET_USER=$USER
mkdir -p ~/.ssh
chmod 700 ~/.ssh

echo "Buscando chaves de https://github.com/${GH_USER}.keys..."
curl -s "https://github.com/${GH_USER}.keys" >> ~/.ssh/authorized_keys

chmod 600 ~/.ssh/authorized_keys
echo "✅ Chaves importadas com sucesso para o usuário $TARGET_USER!"