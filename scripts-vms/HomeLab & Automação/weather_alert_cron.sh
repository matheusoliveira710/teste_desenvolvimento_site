---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "homelab___automa__o"
protocolo: "ARC"
---

#!/bin/bash

Verifica se a temperatura em Campinas excede 30°C

TEMP=$(curl -s "wttr.in/Campinas?format=%t" | sed 's/[^0-9]//g')
if [ "$TEMP" -gt 30 ]; then
echo "ALERTA: Calor extremo em Campinas ($TEMP°C)"
fi