
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

        # Defina o caminho raiz onde seus scripts estão
        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"
        hub = "[[Dashboard_ACVM]]"

        def forcar_hub():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    # Ignora o Dashboard e arquivos não relevantes
                    if file.endswith(('.md', '.sh', '.py', '.yml')) and file != "Dashboard_ACVM.md":
                        path = os.path.join(root, file)
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Remove links internos que criam "clusters" ou "ilhas" (exceto o do Dashboard)
                        # Isso quebra as conexões automáticas entre scripts que fazem o grafo ficar "emaranhado"
                        new_content = re.sub(r'\[\[(?!Dashboard_ACVM)[^\]]+\]\]', '', content)
                
                        # Garante que o link central existe no final do arquivo
                        if "[[Dashboard_ACVM]]" not in new_content:
                            new_content += f"\n\n--- \nHub: {hub}"
                
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"[CONEXÃO FORÇADA]: {file}")

        if __name__ == "__main__":
            forcar_hub()
            print("\n[+] Estrutura em Hub-and-Spoke aplicada.")
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
