import datetime

class Tarefa:
    def __init__(self, titulo, descricao, data, categoria, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.categoria = categoria
        self.status = status
    
    def concluir(self):
        self.status = "Concluída"
    
    def exibir_tarefa(self):
        return(
            f"Título: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Data: {self.data}\n"
            f"Categoria: {self.categoria}\n"
            f"Status: {self.status}\n"
        )