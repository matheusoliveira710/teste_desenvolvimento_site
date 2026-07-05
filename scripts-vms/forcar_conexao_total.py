
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import os

        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa"
        hub_name = "Dashboard_ACVM"

        def forcar_conexao_total():
            for file in os.listdir(root_dir):
                # Seleciona todos os arquivos markdown, exceto o próprio Dashboard
                if file.endswith('.md') and file != f"{hub_name}.md":
                    path = os.path.join(root_dir, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
            
                    # Adiciona o link se não existir
                    if f"[[{hub_name}]]" not in content:
                        with open(path, 'a', encoding='utf-8') as f:
                            f.write(f"\n\n[[{hub_name}]]")
                        print(f"[CONECTADO]: {file}")

        if __name__ == "__main__":
            forcar_conexao_total()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
