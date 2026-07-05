---
dashboard: [[Dashboard_ACVM]]
status: "Operacional"
categoria: "compliance_e_invent_rio"
protocolo: "ARC"
---

#!/bin/bash

Registra atualizações pendentes em log

echo "$(date): Atualizações aplicadas" >> /var/log/package_updates.log
sudo apt list --upgradable >> /var/log/package_updates.log