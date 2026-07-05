import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1519711446445981805/RMb3waFX8JoRFwpgmg32ga5SasqgQsNa7C6J1RcuxU6Ag9Z-fBK2TS_8kl5IxkOPoC70"

def enviar_alerta(titulo, mensagem, nivel="INFO"):
    cores = {"INFO": 3447003, "AVISO": 15844367, "ERRO": 15158332}
    payload = {
        "embeds": [{
            "title": f"[{nivel}] {titulo}",
            "description": mensagem,
            "color": cores.get(nivel, 3447003)
        }]
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"[ERRO]: Falha ao comunicar com Discord: {e}")