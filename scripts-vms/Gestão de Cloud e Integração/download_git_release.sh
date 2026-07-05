---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "gest_o_de_cloud_e_integra__o"
protocolo: "ARC"
---

#!/bin/bash

Baixa a última release de um repo (ex: user/repo)

REPO=$1
if [ -z "$REPO" ]; then echo "Uso: ./download_git_release.sh user/repo"; exit 1; fi
curl -s "https://api.github.com/repos/$REPO/releases/latest" | jq -r .assets[0].browser_download_url | xargs wget