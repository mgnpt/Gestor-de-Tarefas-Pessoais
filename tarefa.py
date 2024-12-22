class Tarefa:
    def __init__(self, titulo, descricao, data, categoria, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
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
    