"""
Intettrface gráfica do
programa para automação de um sistema de alarme de uma escola que
delimita o horário das aulas e intervalos
"""
from Util.TratamentoDeErros import ValidadorHorario
from Dados.armazenamento import GerenciadorDeHorario
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,
    QPushButton, QListWidget, QLineEdit, QLabel, QLineEdit, 
    QTableWidget, QTableWidgetItem
)

class Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.armazenamento = GerenciadorDeHorario()
        self._Horarios = [] #Essa lista vai armazenar os horários que os alarmes deve tocar
        self.setWindowTitle("Controle de Alarmes")
        
        # carregar horários salvos
        self._Horarios = self.armazenamento.carregar_horarios()
        
        layout = QVBoxLayout()

        self.label = QLabel("Digite um horário (HH:MM)")
        layout.addWidget(self.label)

        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)

        self.botao_adicionar = QPushButton("Adicionar horário")
        self.botao_adicionar.clicked.connect(self.adicionar_horario)
        self.entrada.returnPressed.connect(self.botao_adicionar.click)
        layout.addWidget(self.botao_adicionar)

        #Tabela que será mostrado os horários registrados
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(["Horário", "Remover"])
        layout.addWidget(self.tabela)

        self.setLayout(layout)

        self.lista = QListWidget()
        layout.addWidget(self.lista)

        self.setLayout(layout)
        
        # Atualiza a tabela com os horários salvos
        self.atualizar_tabela()
        
    def adicionar_horario(self, horario):
        horario = self.entrada.text()
        validador = ValidadorHorario()

        if horario:
            if validador.verificar_horario(horario):#filtro que garante que o horário foi digitado da maneira correta
                self.entrada.setPlaceholderText("")
                
                linha = self.tabela.rowCount()
                self.tabela.insertRow(linha)

                self.tabela.setItem(linha, 0, QTableWidgetItem(horario))

                botao_remover = QPushButton("Remover")
                botao_remover.clicked.connect(lambda: self.remover_horario(linha))

                self.tabela.setCellWidget(linha, 1, botao_remover)

                hora, minuto = horario.split(":")
                horario = f"{int(hora):02}:{int(minuto):02}"
                #Garante que a hora e os minutos terão dois dígitos

                self._Horarios.append(horario)
                self._Horarios.sort()
                self.atualizar_tabela()
                
                self.armazenamento.salvar_horarios(self._Horarios)

                self.entrada.clear()

            else:
                self.entrada.clear()
                self.entrada.setPlaceholderText("Horário inválido")
    
    def remover_horario(self):

        # Descobre qual botão foi clicado
        botao = self.sender()

        # Descobre em qual posição da tabela o botão está
        index = self.tabela.indexAt(botao.pos())

        # Pega o número da linha
        linha = index.row()

        # Remove da tabela
        self.tabela.removeRow(linha)

        # Remove da lista interna
        self._Horarios.pop(linha)
        self.armazenamento.salvar_horarios(self._Horarios)

    def atualizar_tabela(self):

        # limpa a tabela
        self.tabela.setRowCount(0)

        # percorre os horários
        for i, horario in enumerate(self._Horarios):

            # cria nova linha
            self.tabela.insertRow(i)

            # adiciona o horário na coluna 0
            self.tabela.setItem(i, 0, QTableWidgetItem(horario))

            # cria o botão remover
            botao = QPushButton("Remover")

            # conecta o botão à função
            botao.clicked.connect(self.remover_horario)

            # coloca o botão na coluna 1
            self.tabela.setCellWidget(i, 1, botao)
    
    def get_horarios(self):
        return self._Horarios