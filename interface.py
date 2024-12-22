import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtGui import QFont

class AppWindow(QMainWindow):
    def __init__(self, sistema):
        super().__init__()

        self.sistema = sistema  # Adicionando o sistema de autenticação e registro
        self.setWindowTitle("Gestor de Tarefas Pessoais")
        self.setGeometry(100, 100, 500, 400)

        # Usando QStackedWidget para alternar entre as telas
        self.pages = QStackedWidget()
        self.setCentralWidget(self.pages)

        # Criando as telas
        self.tela_login = self.criar_tela_login()
        self.tela_registo = self.criar_tela_registo()

        # Adicionando as telas ao QStackedWidget
        self.pages.addWidget(self.tela_login)
        self.pages.addWidget(self.tela_registo)

        # Exibindo a tela de login inicialmente
        self.pages.setCurrentWidget(self.tela_login)

    def criar_tela_login(self):
        layout = QVBoxLayout()

        # Mensagem de boas-vindas
        label_bv = QLabel("Login - Gestor de Tarefas Pessoais", self)
        label_bv.setFont(QFont("Arial", 21))
        layout.addWidget(label_bv)

        # Nome de utilizador
        self.input_nome_login = QLineEdit(self)
        self.input_nome_login.setPlaceholderText("Nome de Utilizador")
        layout.addWidget(self.input_nome_login)

        # Senha
        self.input_senha_login = QLineEdit(self)
        self.input_senha_login.setPlaceholderText("Senha")
        self.input_senha_login.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_senha_login)

        # Botão de Login
        btn_login = QPushButton("Login", self)
        btn_login.clicked.connect(self.autenticar_utilizador)
        layout.addWidget(btn_login)

        # Botão de Registo
        btn_registo = QPushButton("Registrar-se", self)
        btn_registo.clicked.connect(self.voltar_para_registro)
        layout.addWidget(btn_registo)

        container = QWidget()
        container.setLayout(layout)
        return container

    def criar_tela_registo(self):
        layout = QVBoxLayout()

        # Título
        label_registro = QLabel("Registo - Gestor de Tarefas Pessoais", self)
        label_registro.setFont(QFont("Arial", 21))
        layout.addWidget(label_registro)

        # Nome de utilizador
        self.input_nome_registro = QLineEdit(self)
        self.input_nome_registro.setPlaceholderText("Nome de Utilizador")
        layout.addWidget(self.input_nome_registro)

        # Senha
        self.input_senha_registro = QLineEdit(self)
        self.input_senha_registro.setPlaceholderText("Senha")
        self.input_senha_registro.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_senha_registro)

        # Botão para registrar
        btn_registrar = QPushButton("Registrar", self)
        btn_registrar.clicked.connect(self.registrar_utilizador)
        layout.addWidget(btn_registrar)

        # Botão para voltar ao Login
        btn_voltar = QPushButton("Voltar ao Login", self)
        btn_voltar.clicked.connect(self.voltar_para_login)
        layout.addWidget(btn_voltar)

        container = QWidget()
        container.setLayout(layout)
        return container

    def autenticar_utilizador(self):
        nome = self.input_nome_login.text()
        senha = self.input_senha_login.text()

        # Verificando se o utilizador existe no sistema
        utilizador = self.sistema.auth_utilizador(nome, senha)
        if utilizador:
            print(f"Bem-vindo, {nome}!")
            # Aqui você pode navegar para a tela principal do sistema após login
        else:
            print("Credenciais inválidas. Tente novamente.")

    def registrar_utilizador(self):
        nome = self.input_nome_registro.text()
        senha = self.input_senha_registro.text()

        # Registrando o novo utilizador
        resultado = self.sistema.reg_utilizador(nome, senha)
        print(resultado)
        # Voltar para a tela de login após registro
        self.pages.setCurrentWidget(self.tela_login)

    def voltar_para_login(self):
        self.pages.setCurrentWidget(self.tela_login)

    def voltar_para_registro(self):
        self.pages.setCurrentWidget(self.tela_registo)


# Código principal para rodar o aplicativo
app = QApplication(sys.argv)
# Inicializando o sistema
sistema = None  # Substitua com a instância de SistemaGestaoTarefas conforme necessário
window = AppWindow(sistema)
window.show()
sys.exit(app.exec_())
