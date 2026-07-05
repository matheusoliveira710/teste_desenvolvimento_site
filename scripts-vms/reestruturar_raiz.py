
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    from lib_pafj.sentinela import enviar_alerta

    try:
        # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
        import os
        import shutil

        # Detecta automaticamente onde o script está rodando
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Define a raiz como um nível acima da pasta atual
        target_dir = os.path.abspath(os.path.join(current_script_dir, '..'))

        def mover_para_raiz():
            print(f"Movendo arquivos de: {current_script_dir}")
            print(f"Para: {target_dir}")
    
            for file in os.listdir(current_script_dir):
                file_path = os.path.join(current_script_dir, file)
        
                # Move apenas arquivos, ignorando o próprio script e pastas
                if os.path.isfile(file_path) and file != "reestruturar_raiz.py":
                    shutil.move(file_path, os.path.join(target_dir, file))
                    print(f"[MOVIDO]: {file} -> Raiz")

            print("\n[+] Migração concluída com sucesso.")

        if __name__ == "__main__":
            mover_para_raiz()
    except Exception as e:
        enviar_alerta("Erro no Script", f"Falha detectada em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
        raise
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
