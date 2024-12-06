import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Nome da janela
        self.setWindowTitle("Gestor de Tarefas Pessoais")
        self.setGeometry(100, 100, 900, 900)

        layout = QVBoxLayout()

        #Mensagem de boas-vindas
        self.BV_label = QLabel("Olá, seja bem-vindo ao Gestor de Tarefas Pessoais!", self)
        self.BV_label.setGeometry(0, 0, 900, 50)
        font = QFont('Arial', 21)
        self.BV_label.setFont(font)
        layout.addWidget(self.BV_label)

        #Caixas de texto debaixo disto
        self.label = QLabel("Introduza os seu dados:", self)
        self.label.setGeometry(0, 0, 900, 100)
        font = QFont('Arial', 17)
        self.label.setFont(font)
        layout.addWidget(self.label)    #Adicionar isto a todos

        #Caixa de texto para o nome
        self.nm_inpt = QLineEdit(self)
        self.nm_inpt.setPlaceholderText("Nome")
        #self.nm_inpt.setGeometry(50, 140, 300, 30)
        layout.addWidget(self.nm_inpt)

        #Caixa de texto para a senha
        self.pws_inpt = QLineEdit(self)
        self.pws_inpt.setPlaceholderText("Senha")
        self.pws_inpt.setEchoMode(QLineEdit.Password)
        #self.pws_inpt.setGeometry(50, 180, 300, 30)
        layout.addWidget(self.pws_inpt)

        #Botão de Login
        self.button = QPushButton("Login", self)
        self.button.setGeometry(50, 230, 150, 40)
        self.button.clicked.connect(self.show_text)

        #Tenho que remover esta parte mas ao fazer isso dou break no design
        layout.addWidget(self.button)
        self.label = QLabel("Nome", self)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def show_text(self):
        self.label.setText(self.text_input.text())
        nome = self.nm_inpt.text()
        password = self.pws_inpt.text()

        if not nome or not password:
            self.label.setText("Por favor, preencha todos os campos.")
        else:
            self.output_label.setText(f"Bem-Vindo, {nome}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
