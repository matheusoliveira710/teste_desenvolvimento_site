
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import os

        # Caminho para a sua pasta de scripts
        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"
        dashboard_link = "[[Dashboard_ACVM]]"

        def reintegra_ao_hub():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    # Pula o próprio Dashboard para não gerar auto-referência infinita
                    if file == "Dashboard_ACVM.md" or not file.endswith(('.md', '.sh', '.py', '.yml')):
                        continue
            
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Se o arquivo já tem YAML, inserimos a linha do dashboard
                    if content.strip().startswith("---"):
                        if "dashboard:" not in content:
                            content = content.replace("---", f"---\ndashboard: {dashboard_link}", 1)
                    else:
                        # Se não tem YAML, criamos um cabeçalho novo
                        header = f"---\ndashboard: {dashboard_link}\n---\n\n"
                        content = header + content

                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"[CONECTADO]: {file}")

        if __name__ == "__main__":
            reintegra_ao_hub()
            print("\n[+] Reintegração concluída. Todos os scripts agora orbitam o Dashboard_ACVM.")
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
