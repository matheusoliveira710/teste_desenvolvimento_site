import os
from lib_pafj.sentinela import enviar_alerta

def executar_esca(vault_path):
    print("[E.S.C.A.]: Iniciando varredura...")
    total_scripts = 0
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".py"):
                total_scripts += 1
    
    enviar_alerta("Protocolo E.S.C.A.", f"Rede mapeada com sucesso. {total_scripts} scripts monitorados.", "INFO")
    return total_scripts