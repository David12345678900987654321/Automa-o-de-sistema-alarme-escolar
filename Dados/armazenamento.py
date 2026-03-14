"""
Este módulo é responsável por salvar os horários registrados e
carregar esses mesmos horários quando o programa é encerrado
"""
import json
import os
from pathlib import Path
import json

class GerenciadorDeHorario:

    def __init__(self):
        self.arquivo = Path(__file__).parent / "horarios.json"

    def salvar_horarios(self, lista):

        with open(self.arquivo, "w") as arquivo:
            json.dump(lista, arquivo)

    def carregar_horarios(self):

        if self.arquivo.exists():

            with open(self.arquivo, "r") as arquivo:
                return json.load(arquivo)

        return []