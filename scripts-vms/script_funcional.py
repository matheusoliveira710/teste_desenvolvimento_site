
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import os

        vault_path = r'C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms'

        def injetar_frontmatter():
            for root, dirs, files in os.walk(vault_path):
                for file in files:
                    if file.endswith(".md") and file != "Dashboard_ACVM.md":
                        file_path = os.path.join(root, file)
                
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                
                        # Adiciona o campo 'hub: [[Dashboard_ACVM]]' no início da nota
                        # Verifica se o frontmatter já existe
                        if content.startswith("---"):
                            new_content = content.replace("---", f"---\nhub: [[Dashboard_ACVM]]", 1)
                        else:
                            new_content = f"---\nhub: [[Dashboard_ACVM]]\n---\n\n" + content
                
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
            print("[PAFJ]: Metadados de conexão injetados com sucesso.")

        if __name__ == "__main__":
            injetar_frontmatter()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
