import os
from tarefa import Tarefa

class Relatorio:
    def __init__(self, filename="relatorio.txt"):
        self.filename = os.path.join(os.getcwd(), filename)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass  # Cria um ficheiro vazio
    
    def gerarRelatorio(self, listaTarefas, utilizador_nome=None, status=None):
        tarefas_relatorio = []

        for tarefa in listaTarefas:
            if status is None or tarefa.status == status:
                tarefas_relatorio.append(f"Utilizador: {utilizador_nome}, Titulo: {tarefa.titulo}, Descricao: {tarefa.descricao}, Categoria: {tarefa.categoria}, Status: {tarefa.status}, Data de criacao: {tarefa.data}\n")

        # Escreve o relatório no ficheiro
        with open(self.filename, "a") as file:
            file.writelines(tarefas_relatorio)