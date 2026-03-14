"""
Este módulo verifica se o horário atual corresponde ao horário digitado
para ativação do alarme, caso sim, será enviado uma mensagem para o
Arduino ESP 8266 para ativar o alarme.
"""
from datetime import datetime
import requests

class VerificadorDeAlarme:

    def __init__(self):
        self.ultimo_alarme = None

    def verificar(self, horarios):

        agora = datetime.now().strftime("%H:%M")

        if agora in horarios and agora != self.ultimo_alarme:
            requests.get("http://alarme.local/alarme")

            self.ultimo_alarme = agora
