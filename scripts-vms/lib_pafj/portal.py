import time
from lib_pafj.sentinela import enviar_alerta

def monitorar_performance(nome_processo, duracao):
    if duracao > 5.0:
        enviar_alerta("Protocolo P.O.R.T.A.L.", f"O processo {nome_processo} excedeu o limite de performance: {duracao:.2f}s", "AVISO")
    else:
        print(f"[P.O.R.T.A.L.]: {nome_processo} rodou em {duracao:.2f}s")