import json
import sys
from pathlib import Path

class GerenciadorDeHorario:

    def __init__(self):
        # Caminho da pasta onde o executável está
        if getattr(sys, 'frozen', False):  # Se estiver rodando como exe
            self.pasta_base = Path(sys.executable).parent
        else:  # Se estiver rodando como script Python
            self.pasta_base = Path(__file__).parent

        self.arquivo = self.pasta_base / "horarios.json"

    def salvar_horarios(self, lista):
        with open(self.arquivo, "w") as arquivo:
            json.dump(lista, arquivo)

    def carregar_horarios(self):

        if self.arquivo.exists():

            with open(self.arquivo, "r") as arquivo:
                return json.load(arquivo)

        return []
