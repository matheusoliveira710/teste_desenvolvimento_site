
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import os
        import re

        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"
        hub = "[[Dashboard_ACVM]]"

        def sanitizar_rede():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file.endswith(('.md', '.sh', '.py', '.yml')) and file != "Dashboard_ACVM.md":
                        path = os.path.join(root, file)
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Regex implacável: remove QUALQUER link, exceto o do Hub
                        # Isso mata as "ilhas" que estão mantendo os clusters unidos
                        sanitized = re.sub(r'\[\[(?!Dashboard_ACVM)[^\]]+\]\]', '', content)
                
                        # Garante a conexão com o Hub
                        if hub not in sanitized:
                            sanitized += f"\n\n--- \nHub: {hub}"
                
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(sanitized)
    
            print("[RELATÓRIO]: Conexões cruzadas destruídas. Apenas o Hub permanece.")

        if __name__ == "__main__":
            sanitizar_rede()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
