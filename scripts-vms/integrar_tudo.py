
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
        hub_link = "[[Dashboard_ACVM]]"

        def integrar_tudo():
            count = 0
            for file in os.listdir(root_dir):
                if file.endswith('.md') and file != "Dashboard_ACVM.md":
                    path = os.path.join(root_dir, file)
                    with open(path, 'r+', encoding='utf-8') as f:
                        content = f.read()
                        # Verifica se já está conectado, se não, adiciona
                        if hub_link not in content:
                            f.write(f"\n\n{hub_link}")
                            count += 1
            print(f"[+] {count} arquivos foram integrados à rede central.")

        if __name__ == "__main__":
            integrar_tudo(),0
    
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
