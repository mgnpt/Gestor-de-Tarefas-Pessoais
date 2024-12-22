class Relatorio:
    def __init__(self, lista_tarefas):
        self.lista_tarefas = lista_tarefas
    
    def criar_relatorio(self, nome_arquivo="relatorio.txt"):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"Relatório de tarefas pendentes - Lista: {self.lista_tarefas.nome}\n")
            arquivo.write("=" * 50 + "\n")

            tarefas_pendentes = []
            for tarefa in self.lista_tarefas.tarefas:
                if tarefa.status == "Pendente":
                    tarefas_pendentes.append(tarefa)

            if not tarefas_pendentes:
                arquivo.write("Nenhuma tarefa pendente encontrada.\n")
            else:
                for tarefa in tarefas_pendentes:
                    arquivo.write(f"Título: {tarefa.titulo}\n")
                    arquivo.write(f"Descrição: {tarefa.descricao}\n")
                    arquivo.write(f"Categoria: {tarefa.categoria}\n")
                    arquivo.write(f"Status: {tarefa.status}\n")
                    arquivo.write("=" * 50 + "\n")
            
            return f'Relatório criado com sucesso em {nome_arquivo}'