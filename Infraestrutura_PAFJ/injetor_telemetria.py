import os

root_dir = r'C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa'

# Linhas de correção de caminho que serão injetadas no topo
path_fix = """
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta
"""

try_block = "\ntry:\n    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---\n"
except_block = """
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
"""

def injetar_telemetria(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "sys.path.append" in content: # Já injetado
        return

    # Indentação do conteúdo original
    indented_content = "\n".join(["    " + line if line.strip() else line for line in content.splitlines()])

    # Monta o arquivo com a correção de rota e a telemetria
    new_content = path_fix + try_block + indented_content + except_block

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"[PAFJ]: Rota e Sentinela injetados em: {os.path.basename(path)}")

# Execução
for root, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.py') and 'lib_pafj' not in root and file != 'injetor_telemetria.py' and file != 'teste_direto.py':
            injetar_telemetria(os.path.join(root, file))