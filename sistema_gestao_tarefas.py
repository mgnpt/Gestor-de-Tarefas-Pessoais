from utilizador import Utilizador
from lista_de_tarefas import ListaDeTarefas

class SistemaGestaoTarefas:
    def __init__(self, ficheiro_utilizadores="profiles.txt"):
        self.ficheiro_utilizadores = ficheiro_utilizadores
        self.utilizadores = {}
        self.ld_utilizadores()  # Carregar os utilizadores do arquivo
    
    # Carregar utilizadores do arquivo
    def ld_utilizadores(self):
        try:
            with open(self.ficheiro_utilizadores, "r") as file:
                for linha in file:
                    nome, senha = linha.strip().split(":")
                    self.utilizadores[nome] = Utilizador(nome, senha)
        except FileNotFoundError:
            print(f"O arquivo {self.ficheiro_utilizadores} não foi encontrado. Nenhum utilizador carregado.")
    
    # Guardar utilizadores no arquivo
    def sv_utilizadores(self):
        with open(self.ficheiro_utilizadores, "w") as file:
            for nome, user in self.utilizadores.items():
                file.write(f"{nome}:{user.senha}\n")
    
    # Registar utilizador
    def reg_utilizador(self, nome, senha):
        if nome in self.utilizadores:
            return f"O utilizador {nome} já existe."
        
        novo_utilizador = Utilizador(nome, senha)
        self.utilizadores[nome] = novo_utilizador
        self.sv_utilizadores()
        return f"Utilizador {nome} criado com sucesso."
    
    # Autenticar utilizador
    def auth_utilizador(self, nome, senha):
        utilizador = self.utilizadores.get(nome)
        if utilizador and utilizador.senha == senha:
            return utilizador
        else:
            return None
    
    # Alterar senha do utilizador
    def alt_senha(self, nome, senha_antiga, senha_nv):
        utilizador = self.utilizadores.get(nome)
        if utilizador and utilizador.senha == senha_antiga:
            utilizador.senha = senha_nv
            self.sv_utilizadores()
            return "Senha alterada com sucesso."
        else:
            return "Nome de utilizador ou senha incorreta"
