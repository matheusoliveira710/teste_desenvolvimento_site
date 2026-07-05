
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import json
        import os

        # Caminho para o graph.json na pasta .obsidian
        graph_config_path = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\.obsidian\graph.json"

        def injetar_config():
            # Estas configurações forçam o motor de física do Obsidian a criar a topologia Estrela
            config = {
                "collapse-filter": False,
                "search": "",
                "showTags": False,
                "showAttachments": False,
                "hideUnresolved": True,
                "showOrphans": False,
                "collapse-color-groups": False,
                "colorGroups": [
                    {
                        "query": "file:Dashboard_ACVM",
                        "color": {"a": 1, "rgb": 14844006}  # Vermelho Vivo
                    }
                ],
                "collapse-forces": True,
                "centerStrength": 0.3,   # Força o centro a ser atraente
                "repelStrength": 2.0,    # Aumenta a repulsão entre nós, quebrando clusters
                "linkStrength": 0.8,     # Força a atração do link central
                "linkDistance": 250      # Espaçamento para criar a órbita
            }

            # Garantir que o diretório existe e salvar o novo config
            os.makedirs(os.path.dirname(graph_config_path), exist_ok=True)
            with open(graph_config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
    
            print("[STATUS]: Configurações de topologia em ESTRELA injetadas com sucesso.")

        if __name__ == "__main__":
            injetar_config()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
