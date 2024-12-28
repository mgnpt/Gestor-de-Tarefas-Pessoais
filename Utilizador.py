from lista_de_tarefas import ListaDeTarefas
class Utilizador:
    def __init__(self, nome, senha):    #Pefil atual
        self.__nome = nome
        self.__senha = senha
        self.lista_tarefas = ListaDeTarefas(nome)

    def __str__(self):
        return f"{self.__nome}:{self.__senha}"
    
    def save(profile):    #Função para guardar os perfis
        with open("profiles.txt", "a") as file:
            file.write(f"{profile.__str__()}\n")

    def load(self):   #Função para carregar os perfis
        profiles = []
        try:
            with open("profiles.txt", "r") as file:
                for linha in file:
                    nome, senha = linha.strip().split(":")
                    profiles.append(Utilizador(nome, senha))
        except FileNotFoundError:
            print("Arquivo de perfis não encontrado. Nenhum perfil foi carregado.")
        return profiles

    def alt_senha(self, nv_senha):    #Função para alterar a passe de um dos perfis
        self.__senha = nv_senha
        profiles = Utilizador.load()
        with open("profiles.txt", "w") as file:
            for profile in profiles:
                if profile.__Utilizador__nome == self.__nome:
                    file.write(f"{self.__nome}:{self.__senha}")
                else:
                    file.write(f"{profile._Utilizador__nome}:{profile._Utilizador__senha}\n")
