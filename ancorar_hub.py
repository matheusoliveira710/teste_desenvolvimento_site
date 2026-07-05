
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import os

        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"
        link_ancora = "\n\n---\n**Hub de Comando:** [[Dashboard_ACVM]]"

        def ancorar_no_hub():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file == "Dashboard_ACVM.md" or not file.endswith(('.md', '.sh', '.py', '.yml')):
                        continue
            
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Evita duplicar a âncora
                    if "[[Dashboard_ACVM]]" not in content:
                        with open(path, 'a', encoding='utf-8') as f:
                            f.write(link_ancora)
                        print(f"[ANCORADO]: {file}")

        if __name__ == "__main__":
            ancorar_no_hub()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
