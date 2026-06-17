#!/bin/bash
echo "🔑 Gerando par de chaves SSH (ED25519)..."
echo "Digite o seu e-mail ou comentário para a chave:"
read -r COMMENT
mkdir -p ~/.ssh
chmod 700 ~/.ssh
ssh-keygen -t ed25519 -C "$COMMENT" -f ~/.ssh/id_ed25519_lab -N ""
chmod 600 ~/.ssh/id_ed25519_lab
chmod 644 ~/.ssh/id_ed25519_lab.pub
echo "✅ Chaves geradas em ~/.ssh/id_ed25519_lab"