import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QComboBox, QDialog, QMessageBox
from PyQt5.QtGui import QFont
from sistema_gestao_tarefas import SistemaGestaoTarefas
from tarefa import Tarefa


class AppWindow(QMainWindow):
    def __init__(self, sistema):
        super().__init__()

        self.sistema = sistema
        self.nome_atual = None

        self.setWindowTitle("Gestor de Tarefas Pessoais")
        self.setGeometry(100, 100, 500, 400)

        self.pages = QStackedWidget()
        self.setCentralWidget(self.pages)

        #Criar telas
        self.tela_login = self.criar_tela_login()
        self.tela_registo = self.criar_tela_registo()

        self.pages.addWidget(self.tela_login)
        self.pages.addWidget(self.tela_registo)

        #Iniciar na tela de login
        self.pages.setCurrentWidget(self.tela_login)

    def criar_tela_login(self):
        layout = QVBoxLayout()

        #Mensagem de boas-vindas
        label_bv = QLabel("Login - Gestor de Tarefas Pessoais", self)
        label_bv.setFont(QFont("Arial", 21))
        layout.addWidget(label_bv)

        #Nome de utilizador
        self.input_nome_login = QLineEdit(self)
        self.input_nome_login.setPlaceholderText("Nome de Utilizador")
        layout.addWidget(self.input_nome_login)

        #Password
        self.input_senha_login = QLineEdit(self)
        self.input_senha_login.setPlaceholderText("Senha")
        self.input_senha_login.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_senha_login)

        #Botão de Login
        btn_login = QPushButton("Login", self)
        btn_login.clicked.connect(self.autenticar_utilizador)
        layout.addWidget(btn_login)

        #Botão de Registo
        btn_registo = QPushButton("Registrar-se", self)
        btn_registo.clicked.connect(self.voltar_para_registro)
        layout.addWidget(btn_registo)

        container = QWidget()
        container.setLayout(layout)
        return container

    def criar_tela_registo(self):
        layout = QVBoxLayout()

        #Título
        label_registro = QLabel("Registo - Gestor de Tarefas Pessoais", self)
        label_registro.setFont(QFont("Arial", 21))
        layout.addWidget(label_registro)

        #Nome de utilizador
        self.input_nome_registro = QLineEdit(self)
        self.input_nome_registro.setPlaceholderText("Nome de Utilizador")
        layout.addWidget(self.input_nome_registro)

        #Senha
        self.input_senha_registro = QLineEdit(self)
        self.input_senha_registro.setPlaceholderText("Senha")
        self.input_senha_registro.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_senha_registro)

        #Botão para registrar
        btn_registrar = QPushButton("Registrar", self)
        btn_registrar.clicked.connect(self.registrar_utilizador)
        layout.addWidget(btn_registrar)

        #Botão para voltar ao Login
        btn_voltar = QPushButton("Voltar ao Login", self)
        btn_voltar.clicked.connect(self.voltar_para_login)
        layout.addWidget(btn_voltar)

        container = QWidget()
        container.setLayout(layout)
        return container
    
    def criar_tela_dashboard(self, nome):
        layout = QVBoxLayout()

        #Mensagem de boas-vindas
        label_bv = QLabel(f"Bem-vindo, {nome}!", self)
        label_bv.setFont(QFont("Arial", 21))
        layout.addWidget(label_bv)

        #Botão para ver tarefas
        btn_ver_tarefas = QPushButton("Ver lista de tarefas", self)
        btn_ver_tarefas.clicked.connect(self.mostrar_lista_tarefas)
        layout.addWidget(btn_ver_tarefas)

        #Botão logout
        btn_logout = QPushButton("Logout", self)
        btn_logout.clicked.connect(self.voltar_para_login)
        layout.addWidget(btn_logout)

        container = QWidget()
        container.setLayout(layout)
        return container

    def mostrar_lista_tarefas(self):
        utilizador = self.sistema.utilizadores.get(self.nome_atual)
        if utilizador:
            self.ver_lista_tarefas(utilizador.lista_tarefas)
        else:
           print("Erro: utilizador não encontrado.") 

    def ver_lista_tarefas(self, lista_de_tarefas):
        layout = QVBoxLayout()

        label_titulo = QLabel("Lista de Tarefas", self)
        label_titulo.setFont(QFont("Arial", 18))
        layout.addWidget(label_titulo)

        if lista_de_tarefas.tarefas:
            for tarefa in lista_de_tarefas.tarefas:
                label_tarefa = QLabel(f"- {tarefa.titulo}: {tarefa.descricao}", self)
                layout.addWidget(label_tarefa)
        else:
            label_vazio = QLabel("A lista está vazia", self)
            layout.addWidget(label_vazio)
        
        btn_criar_tarefa = QPushButton("Criar Tarefa", self)
        btn_criar_tarefa.clicked.connect(self.criar_tarefa)
        layout.addWidget(btn_criar_tarefa)

        btn_voltar = QPushButton("Voltar", self)
        btn_voltar.clicked.connect(self.voltar_para_dashboard)
        layout.addWidget(btn_voltar)

        btn_voltar = QPushButton("Voltar", self)
        btn_voltar.clicked.connect(self.voltar_para_dashboard)
        layout.addWidget(btn_voltar)

        container = QWidget()
        container.setLayout(layout)
        self.pages.addWidget(container)
        self.pages.setCurrentWidget(container)
    
    def criar_tarefa(self):
        self.nv_tarefa_janela = QDialog(self)
        self.nv_tarefa_janela.setWindowTitle("Criar Tarefa")

        layout = QVBoxLayout()

        #Título
        self.input_titulo = QLineEdit()
        self.input_titulo.setPlaceholderText("Titulo")
        layout.addWidget(self.input_titulo)

        #Descrição
        self.input_descricao = QLineEdit()
        self.input_descricao.setPlaceholderText("Descricao")
        layout.addWidget(self.input_descricao)

        #Data
        self.input_data = QLineEdit()
        self.input_data.setPlaceholderText("Data (ex: 2024-12-28)")
        layout.addWidget(self.input_data)

        #Categoria
        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems(["Trabalho", "Pessoal", "Estudos"])
        layout.addWidget(self.combo_categoria)

        self.combo_status = QComboBox()
        self.combo_status.addItems(["Pendente", "Concluida"])
        layout.addWidget(self.combo_status)

        btn_salvar = QPushButton("Salvar", self)
        btn_salvar.clicked.connect(self.salvar_tarefa)
        layout.addWidget(btn_salvar)

        btn_cancelar = QPushButton("Cancelar", self)
        btn_cancelar.clicked.connect(self.nv_tarefa_janela.close)
        layout.addWidget(btn_cancelar)

        self.nv_tarefa_janela.setLayout(layout)
        self.nv_tarefa_janela.exec_()

    def salvar_tarefa(self):
        titulo = self.input_titulo.text()
        descricao = self.input_descricao.text()
        data = self.input_data.text()
        categoria = self.combo_categoria.currentText()

        if not titulo or not descricao or not data or not categoria:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos")
            return
        
        utilizador = self.sistema.utilizadores.get(self.nome_atual)

        if utilizador:
           utilizador.lista_tarefas.adicionar_tarefa(titulo, descricao, data, categoria)
           QMessageBox.information(self, "Sucesso", "Tarefa criada com sucesso!")
           self.nv_tarefa_janela.close()

        else:
            QMessageBox.critical(self, "Erro", "Não foi possível criar a tarefa. Utilizador nao encontrado.")

    def voltar_para_dashboard(self):
        self.pages.setCurrentWidget(self.tela_dashboard)

    def autenticar_utilizador(self):
        nome = self.input_nome_login.text()
        senha = self.input_senha_login.text()

        utilizador = self.sistema.auth_utilizador(nome, senha)
        if utilizador:
            print(f"Bem-vindo, {nome}!")
            self.nome_atual = nome
            if not hasattr(self, 'tela_dashboard'):
                self.tela_dashboard = self.criar_tela_dashboard(nome)
                self.pages.addWidget(self.tela_dashboard)
            self.pages.setCurrentWidget(self.tela_dashboard)
        else:
            print("Credenciais inválidas. Tente novamente.")
            

    def registrar_utilizador(self):
        nome = self.input_nome_registro.text()
        senha = self.input_senha_registro.text()

        #Criar novo utilizador
        resultado = self.sistema.reg_utilizador(nome, senha)
        print(resultado)
        #Voltar para a tela de login após registro
        self.pages.setCurrentWidget(self.tela_login)

    def voltar_para_login(self):
        self.pages.setCurrentWidget(self.tela_login)

    def voltar_para_registro(self):
        self.pages.setCurrentWidget(self.tela_registo)
    
    def criar_relatorio(self):
        utilizador = self.sistema.utilizadores.get(self.nome_atual)
        if utilizador:
            from relatorio import Relatorio
            relatorio = Relatorio(utilizador.lista_tarefas)
            resultado = relatorio.criar_relatorio()
            QMessageBox.information(self, "Relatório", resultado)
        else:
            QMessageBox.critical(self, "Erro", "Erro ao criar o relatório. Utilizador nao encontrado.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sistema = SistemaGestaoTarefas(ficheiro_utilizadores="profiles.txt")
    window = AppWindow(sistema)
    window.show()
    sys.exit(app.exec_())

