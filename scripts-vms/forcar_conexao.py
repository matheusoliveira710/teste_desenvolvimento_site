
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import os

        # Caminho da raiz do seu cofre
        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa"
        hub_file = "Dashboard_ACVM.md"

        def forcar_conexao():
            for file in os.listdir(root_dir):
                if file.endswith('.md') and file != hub_file:
                    path = os.path.join(root_dir, file)
                    with open(path, 'a', encoding='utf-8') as f:
                        # Adiciona o link explicitamente no final do arquivo
                        f.write(f"\n\n# Conexão Central\n[[{hub_file.replace('.md', '')}]]")
            print("[+] Conexões forçadas com sucesso.")

        if __name__ == "__main__":
            forcar_conexao()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
