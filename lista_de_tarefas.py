from tarefa import Tarefa

class ListaDeTarefas:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
    
    def remover_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                self.tarefas.remove(tarefa)
                return f"Tarefa '{titulo}' foi removida com sucesso!"
        return f"Tarefa '{titulo}' nao encontrada na lista!"
    
    def lista_tarefas(self):
        if not self.tarefas:
            return f"A lista '{self.nome}' está vazia"
        
        resultado = ""
        for tarefa in self.tarefas:
            resultado += tarefa.exibir_tarefa() + "\n"
        
        return  resultado.strip()