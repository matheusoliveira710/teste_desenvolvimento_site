---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "seguran_a_e_hardening"
protocolo: "ARC"
---

#!/bin/bash

Monitora o uso de sudo nos logs do sistema

echo "--- Monitoramento de Uso de SUDO (Últimas 20 linhas) ---"
grep "sudo" /var/log/auth.log | tail -n 20