
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

        # Caminho raiz
        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"
        dashboard_link = "[[Dashboard_ACVM]]"

        def reintegra_tudo():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    # Ignora o próprio Dashboard e arquivos que não são scripts/notas
                    if file == "Dashboard_ACVM.md" or not file.endswith(('.sh', '.ps1', '.py', '.yml', '.md')):
                        continue
            
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Adiciona o link do Dashboard ao YAML de forma limpa
                    if "---" in content:
                        if "dashboard: " not in content:
                            content = content.replace("---", f"---\ndashboard: {dashboard_link}", 1)
                    else:
                        content = f"---\ndashboard: {dashboard_link}\n---\n\n" + content

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"[CONECTADO]: {file}")

        if __name__ == "__main__":
            reintegra_tudo()
    
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
