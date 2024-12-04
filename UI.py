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

        #Caixas de texto debaixo disto
        self.label = QLabel("Introduza os seu dados:", self)
        self.label.setGeometry(0, 0, 900, 100)
        font = QFont('Arial', 17)
        self.label.setFont(font)

        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        #Botão
        self.button = QPushButton("Login", self)
        self.button.clicked.connect(self.show_text)

        layout.addWidget(self.button)
        self.label = QLabel("Nome", self)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def show_text(self):
        self.label.setText(self.text_input.text())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
