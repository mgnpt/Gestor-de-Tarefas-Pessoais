import bcrypt
from lista_de_tarefas import ListaDeTarefas

class Utilizador:
    
    #Pefil atual
    def __init__(self, nome, senha):    
        self.__nome = nome
        self.__senha = senha
        self.lista_tarefas = ListaDeTarefas(nome)

    def get_senha(self):
        return self.__senha

    #Método para verificar a senha fornecida
    def verificar_senha(self, senha_tentativa):
        return bcrypt.checkpw(senha_tentativa.encode(), self.senha)
    
    def __str__(self):
        return f"{self.__nome}:{self.__senha}"
    
    #Função para guardar os perfis
    def save(profile):    
        with open("profiles.txt", "a") as file:
            file.write(f"{profile.__str__()}\n")

    #Função para carregar os perfis
    def load(self):   
        return load_profiles()

    #Função para alterar a passe de um dos perfis
    def alt_senha(self, nv_senha):    
        self.__senha = bcrypt.hashpw(nv_senha.encode(), bcrypt.gensalt()).decode()
        profiles = load_profiles()
        with open("profiles.txt", "w") as file:
            for profile in profiles:
                if profile.__nome == self.__nome:
                    file.write(f"{self.__nome}:{self.__senha}\n")
                else:
                    file.write(f"{profile.__nome}:{profile.__senha}\n")

#Função para carregar os perfis
def load_profiles():
    profiles = []
    try:
        with open("profiles.txt", "r") as file:
            for linha in file:
                nome, senha = linha.strip().split(":")
                profiles.append(Utilizador(nome, senha))
    except FileNotFoundError:
        print("Arquivo de perfis não encontrado. Nenhum perfil foi carregado.")
    return profiles
