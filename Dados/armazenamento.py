"""
Este módulo é responsável por salvar os horários registrados e
carregar esses mesmos horários quando o programa é encerrado
"""
import json
import os
class GerenciadorDeHorario:
    def salvar_horarios(self, lista):

        with open("horarios.json", "w") as arquivo:
            json.dump(lista, arquivo)


    def carregar_horarios(self):

        if os.path.exists("horarios.json"):

            with open("horarios.json", "r") as arquivo:
                return json.load(arquivo)

        return []