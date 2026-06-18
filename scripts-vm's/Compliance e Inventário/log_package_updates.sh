#!/bin/bash

Registra atualizações pendentes em log

echo "$(date): Atualizações aplicadas" >> /var/log/package_updates.log
sudo apt list --upgradable >> /var/log/package_updates.log