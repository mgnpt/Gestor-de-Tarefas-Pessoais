from utilizador import Utilizador
from lista_de_tarefas import ListaDeTarefas
from relatorio import Relatorio
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
                    linha = linha.strip()
                    if ":" in linha:
                        nome, senha = linha.split(":")
                        self.utilizadores[nome] = Utilizador(nome, senha)
                    else:
                        print(f"Formato de linha inválido: {linha} (foi ignorado)")
            print(f"Utilizadores carregados: {list(self.utilizadores.keys())}")
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
        if utilizador and utilizador._Utilizador__senha == senha:
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
    
    def cr_relatorio(self, nome_utilizador, nome_arquivo="relatorio.txt"):
        if nome_utilizador in self.utilizadores:
            utilizador = self.utilizadores[nome_utilizador]
            relatorio = Relatorio(utilizador.lista_tarefas)
            return relatorio.criar_relatorio(nome_arquivo)
        else:
            return "Utilizador nao encontrado."