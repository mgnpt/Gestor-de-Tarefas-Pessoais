import os
from tarefa import Tarefa

class ListaDeTarefas:
    def __init__(self, username):
        self.username = username
        self.tarefas =[]
        self.filename = os.path.join(os.getcwd(), "tarefa.txt")
        if not os.path.exists(self.filename): 
            with open(self.filename, "w") as file:
                pass  # Cria um ficheiro vazio

    def adicionarTarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)
        with open(self.filename, "a") as file:
            file.write(f"Utilizador: {self.username},Titulo: {tarefa.titulo} Descricao: {tarefa.descricao}, Categoria: {tarefa.categoria}, Status: {tarefa.status},Data de criação: {tarefa.data}\n")

    def removerTarefa(self, titulo):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.titulo != titulo]
        with open(self.filename,"w") as file:
            for tarefa in self.tarefas:
                file.write(f"Utilizador: {self.username},Titulo: {tarefa.titulo} Descricao: {tarefa.descricao}, Categoria: {tarefa.categoria}, Status: {tarefa.status},Data de criação: {tarefa.data}\n")
    
    def lista_tarefas(self):
        if not self.tarefas:
            return f"A lista '{self.nome}' está vazia"
        
        resultado = ""
        for tarefa in self.tarefas:
            resultado += tarefa.exibir_tarefa() + "\n"
        
        return  resultado.strip()
    