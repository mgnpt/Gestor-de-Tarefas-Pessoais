import bcrypt
from utilizador import Utilizador
import os

class SistemaGestaoTarefas:
    def __init__(self, ficheiro_utilizadores="profiles.txt"):
        self.ficheiro_utilizadores = os.path.join(os.getcwd(), ficheiro_utilizadores)
        if not os.path.exists(self.ficheiro_utilizadores): 
            with open(self.ficheiro_utilizadores, "w") as file:
                pass  # Cria um ficheiro vazio
        self.ficheiro_utilizadores = ficheiro_utilizadores
        self.utilizadores = {}
        self.ld_utilizadores()  # Carregar os utilizadores do arquivo
    
    # Carregar utilizadores do arquivo
    def ld_utilizadores(self):
        with open(self.ficheiro_utilizadores, "r") as file:
            for linha in file:
                linha = linha.strip()
                if ":" in linha:
                    nomeGuardado, senhaGuardada = linha.split(":")
                    senhaGuardada = senhaGuardada.strip().encode()  # Converter senha para bytes
                    self.utilizadores[nomeGuardado] = Utilizador(nomeGuardado, senhaGuardada)


    # Registar utilizador
    def reg_utilizador(self, nome, senha):
        if nome in self.utilizadores:
            return f"O utilizador {nome} já existe."
        senhaEncriptada = self.encriptarSenha(senha)
        self.utilizadores[nome] = Utilizador(nome, senhaEncriptada)
        with open("profiles.txt","a") as file:
            file.write(f"{nome}:{senhaEncriptada.decode()}\n")
        return f"Utilizador {nome} criado com sucesso."
        

    # Autenticar utilizador
    def auth_utilizador(self, nome, senha):
        utilizador = self.utilizadores.get(nome)
        if utilizador and bcrypt.checkpw(senha.encode(), utilizador.get_senha()):
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
    
    
    
    def encriptarSenha(self,senha):
        return bcrypt.hashpw(senha.encode(), bcrypt.gensalt())