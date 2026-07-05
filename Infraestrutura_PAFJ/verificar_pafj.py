import os
import sys

# PATCH: Garante que a raiz do projeto seja reconhecida pelo importador
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def verificar_integridade():
    print("[V.E.R.I.F.A.]: Iniciando varredura de integridade...")
    
    # Define caminhos
    root_dir = os.getcwd()
    lib_path = os.path.join(root_dir, "lib_pafj")
    
    # 1. Verifica pasta lib_pafj
    if not os.path.exists(lib_path):
        print("[ERRO]: Pasta 'lib_pafj' não encontrada na raiz.")
        return
    
    # 2. Verifica arquivos obrigatórios
    arquivos_necessarios = ["__init__.py", "sentinela.py", "esca.py", "portal.py"]
    for arq in arquivos_necessarios:
        caminho_arq = os.path.join(lib_path, arq)
        if not os.path.exists(caminho_arq):
            print(f"[ERRO]: Arquivo '{arq}' ausente em lib_pafj.")
            return
        else:
            print(f"[OK]: {arq} detectado.")
            
    print("\n[SUCESSO]: Estrutura PAFJ validada. Tudo pronto para operações de alto nível.")
    
    # Teste de disparo para o S.E.N.T.I.N.E.L.A.
    try:
        from lib_pafj.sentinela import enviar_alerta
        enviar_alerta("Protocolo S.E.N.T.I.N.E.L.A.", "Sistema online e comunicando com o Discord. Integridade validada.", "INFO")
        print("[SUCESSO]: Alerta de teste enviado ao Discord.")
    except Exception as e:
        print(f"[ERRO]: Falha ao disparar alerta de teste: {e}")

if __name__ == "__main__":
    verificar_integridade()
