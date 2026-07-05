
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

        # RECOMENDAÇÃO: Renomeie a pasta no Windows para "scripts-vms" (sem o apóstrofo)
        # Se renomear, atualize esta linha:
        root_dir = r"C:\Users\Matheus\PycharmProjects\PythonProject\teste_site_empresa\scripts-vms"

        yaml_template = """---
        status: "Operacional"
        categoria: "{categoria}"
        protocolo: "{protocolo}"
        dashboard: "[[Dashboard_ACVM]]"
        ---
        """

        def sanitize_category(name):
            return re.sub(r'[^a-zA-Z0-9]', '_', name).lower()

        def get_protocolo_por_categoria(categoria):
            mapping = {
                'seguran_a_e_hardening': 'S.H.I.E.L.D.',
                'monitoramento': 'C.O.R.E.S.',
                'automations_e_ci_cd': 'A.T.L.A.S.',
                'governan_a_de_rede': 'W.A.L.L.',
                'self_healing': 'P.U.R.G.E.',
                'banco_de_dados': 'B.R.I.D.G.E.',
                'rede': 'P.I.N.G.'
            }
            return mapping.get(categoria, 'A.R.C.')

        def processar_arquivos():
            for root, dirs, files in os.walk(root_dir):
                # Evita processar pastas ocultas
                if '.obsidian' in root or '.git' in root:
                    continue
            
                # Define a categoria e protocolo baseando-se na pasta atual
                raw_category = os.path.basename(root)
                clean_category = sanitize_category(raw_category)
                protocolo_ativo = get_protocolo_por_categoria(clean_category)
        
                for file in files:
                    if file.endswith(('.sh', '.ps1', '.bat', '.py')):
                        file_path = os.path.join(root, file)
                
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Remove o link antigo do índice
                        new_content = content.replace("Voltar ao Índice Central", "")
                
                        # Se não houver cabeçalho, adiciona. Se houver, apenas atualiza o conteúdo sem o link velho
                        if not new_content.strip().startswith("---"):
                            header = yaml_template.format(categoria=clean_category, protocolo=protocolo_ativo)
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(header + new_content)
                        else:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                
                        print(f"Processado: {file} | Categoria: {clean_category}")

        if __name__ == "__main__":
            processar_arquivos()
            print("\n[+] Processo concluído com integridade. Estrutura A.R.C. sincronizada.")
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
