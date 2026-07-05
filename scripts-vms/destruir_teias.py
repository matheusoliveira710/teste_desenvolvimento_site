
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

        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa"
        hub = "[[Dashboard_ACVM]]"

        def destruir_teias():
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file.endswith('.md') and file != "Dashboard_ACVM.md":
                        path = os.path.join(root, file)
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Regex: remove qualquer link que NÃO seja o Dashboard
                        # Isso quebra as teias que formam os triângulos e clusters
                        novo_conteudo = re.sub(r'\[\[(?!Dashboard_ACVM)[^\]]+\]\]', '', content)
                
                        # Garante o link único para o Hub
                        if hub not in novo_conteudo:
                            novo_conteudo += f"\n\n---\nHub: {hub}"
                
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(novo_conteudo)
            print("[RELATÓRIO]: Todas as conexões laterais foram cortadas. A rede está puramente radial.")

        if __name__ == "__main__":
            destruir_teias()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
