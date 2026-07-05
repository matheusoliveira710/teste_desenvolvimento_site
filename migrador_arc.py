
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
        import re

        # Defina o caminho raiz da sua pasta de scripts (sem o apóstrofo)
        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"

        def migrar_arquivos():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file.endswith(('.sh', '.ps1', '.py', '.yml', '.md')):
                        file_path = os.path.join(root, file)
                
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # 1. Remove qualquer menção ao índice antigo
                
                        # 2. Garante que o cabeçalho YAML existe e está no padrão A.R.C.
                        # Se não tem ---, criamos. Se tem, inserimos o link do dashboard.
                        if content.strip().startswith("---"):
                            # Se já tem YAML, garantimos a linha do dashboard
                            if "dashboard: " not in content:
                                content = content.replace("---", "---\ndashboard: \"[[Dashboard_ACVM]]\"", 1)
                        else:
                            # Se não tem YAML, criamos um novo
                            header = "---\ndashboard: \"[[Dashboard_ACVM]]\"\n---\n\n"
                            content = header + content

                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                
                        print(f"[OK] Migrado: {file}")

        if __name__ == "__main__":
            migrar_arquivos()
            print("\n[+] Migração concluída. O Dashboard_ACVM agora é o seu Hub central.")
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
