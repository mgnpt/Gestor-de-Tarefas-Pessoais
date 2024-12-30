import datetime, os

class Tarefa:
    def __init__(self, titulo, descricao, data, categoria, status):
        self.titulo = titulo
        self.descricao = descricao
        self.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.categoria = categoria
        self.status = status
    
    def concluir(self):
        self.status = "Concluída"
                
def ld_tarefas():
    tasks = []
    if os.path.exists("tarefa.txt"):
        with open("tarefa.txt", "r") as file:
                for line in file:
                    nome_utilizador, titulo, descricao, categoria, status = line.strip().split(",")
                    tasks.append(Tarefa(nome_utilizador, titulo, descricao, categoria, status))
        return tasks