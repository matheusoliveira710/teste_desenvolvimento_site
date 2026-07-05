
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

        # Defina o caminho raiz dos seus scripts
        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"
        hub_link = "[[Dashboard_ACVM]]"

        def centralizar_rede():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    # Filtra apenas arquivos de código/markdown relevantes
                    if file.endswith(('.md', '.sh', '.py', '.yml')) and file != "Dashboard_ACVM.md":
                        path = os.path.join(root, file)
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # 1. Remove qualquer link interno que não seja para o Dashboard
                        # Isso mata as conexões cruzadas que formam as ilhas
                        sanitized = re.sub(r'\[\[(?!Dashboard_ACVM)[^\]]+\]\]', '', content)
                
                        # 2. Garante que o link do Dashboard exista no final do arquivo
                        # Se já existir, não adicionamos duplicado
                        if hub_link not in sanitized:
                            sanitized += f"\n\n---\nHub: {hub_link}"
                
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(sanitized)
                
                        print(f"[CENTRALIZADO]: {file}")

        if __name__ == "__main__":
            centralizar_rede()
            print("\n[+] Todos os scripts foram apontados para o Dashboard_ACVM.")
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
