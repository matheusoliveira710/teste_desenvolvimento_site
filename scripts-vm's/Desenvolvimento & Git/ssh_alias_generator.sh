#!/bin/bash

Adiciona apelido SSH no config

read -p "Apelido: " alias
read -p "IP: " ip
read -p "User: " user
echo -e "\nHost $alias\n  HostName $ip\n  User $user" >> ~/.ssh/config
echo "Alias adicionado com sucesso!"