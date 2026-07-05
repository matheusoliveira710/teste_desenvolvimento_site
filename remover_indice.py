
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        ---
        dashboard: [[Dashboard_ACVM]]
        ---

        import os

        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa"

        def expurgar_indice():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file.endswith(('.md', '.sh', '.py', '.yml')):
                        path = os.path.join(root, file)
                        with open(path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                
                        with open(path, 'w', encoding='utf-8') as f:
                            for line in lines:
                                    f.write(line)

        expurgar_indice()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
