---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "automations_e_ci_cd"
protocolo: "ARC"
---

#!/bin/bash
# Altere os valores abaixo de acordo com as configurações do seu repositório do GitHub
RUNNER_VERSION="2.317.0" # Altere se necessário para a versão atualizada
RUNNER_URL="https://github.com/SEU_USUARIO/SEU_REPOSITORIO"
RUNNER_TOKEN="SEU_TOKEN_DO_GITHUB_RUNNER"

echo "🚀 Configurando Self-Hosted GitHub Runner..."
mkdir -p ~/actions-runner && cd ~/actions-runner || exit
curl -o actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz
tar xzf ./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz

./config.sh --url "$RUNNER_URL" --token "$RUNNER_TOKEN" --unattended
sudo ./svc.sh install
sudo ./svc.sh start
echo "✅ GitHub Runner instalado e rodando em background!"