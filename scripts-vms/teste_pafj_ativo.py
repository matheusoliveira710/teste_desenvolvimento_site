
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib_pafj.sentinela import enviar_alerta

try:
    # --- INÍCIO DA EXECUÇÃO DO PROCESSO ---
    # Este script testará se a injeção automática funcionou
    try:
        print("Iniciando teste de notificação automática...")
        # Causando erro proposital para disparar o Sentinela
        resultado = 1 / 0
    except Exception as e:
        # O bloco injetado deve capturar isso e enviar para o Discord
        # Se o script foi injetado corretamente, ele terá o bloco except automático.
        # Mas como este é um script novo, vamos disparar manualmente para garantir:
        from lib_pafj.sentinela import enviar_alerta
        enviar_alerta("Teste de Comunicação", f"O sistema está operando corretamente. Erro capturado: {str(e)}", "INFO")
        print("Alerta enviado ao Discord!")
except Exception as e:
    enviar_alerta("Erro no Script", f"Falha em: {os.path.basename(__file__)} - Erro: {str(e)}", "ERRO")
    raise
