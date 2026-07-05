
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

        def reconstruir_conexoes():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file.endswith(('.md', '.sh', '.py', '.yml')) and file != "Dashboard_ACVM.md":
                        file_path = os.path.join(root, file)
                
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Remove QUALQUER link que não seja o Dashboard
                        new_content = re.sub(r'\[\[(?!Dashboard_ACVM)[^\]]+\]\]', '', content)
                
                        # Garante que o link do Dashboard exista no final
                        if "[[Dashboard_ACVM]]" not in new_content:
                            new_content += "\n\n--- \nHub: [[Dashboard_ACVM]]"
                
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"[CONEXÃO FORÇADA]: {file}")

        if __name__ == "__main__":
            reconstruir_conexoes()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
