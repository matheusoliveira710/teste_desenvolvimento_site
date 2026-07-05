from lib_pafj.sentinela import enviar_alerta

try:
    print("Iniciando teste de comunicação...")
    raise Exception("Disparo manual do Sentinela")
except Exception as e:
    enviar_alerta("Teste de Comunicação", f"Erro: {str(e)}", "ERRO")
    print("Alerta disparado!")