---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "seguran_a_dados"
protocolo: "ARC"
---

#!/bin/bash

Mostra os últimos 10 logins no sistema

echo "--- Relatório de Últimos Logins ---"
last | head -n 10