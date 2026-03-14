"""
Programa para automação de um sistema de alarme de uma escola que
delimita o horário das aulas e intervalos
"""
from Core.Controller import SistemaAlarme

if __name__ == "__main__":
    sistema = SistemaAlarme()
    sistema.executar()