"""
Programa para automação de um sistema de alarme de uma escola que
delimita o horário das aulas e intervalos
"""
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from Interface.Interface_Grafica import Janela
from Core.VerificadorDeHorarios import VerificadorDeAlarme

class SistemaAlarme:

    def __init__(self):

        self.app = QApplication(sys.argv)
        # cria a interface
        self.janela = Janela()

        # cria o timer que verifica os horários
        self.verificador = VerificadorDeAlarme()

        self.timer = QTimer()
        self.timer.timeout.connect(self.verificar)

        # executa a cada 1 segundo
        self.timer.start(1000)

    def verificar(self):
        horarios = self.janela.get_horarios()
        self.verificador.verificar(horarios)

    def executar(self):
        self.janela.show()
        sys.exit(self.app.exec())