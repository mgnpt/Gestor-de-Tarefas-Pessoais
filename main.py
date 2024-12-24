import sys
from PyQt5.QtWidgets import QApplication
from sistema_gestao_tarefas import SistemaGestaoTarefas
from interface import AppWindow

#'''''
def main():
    sistema = SistemaGestaoTarefas(ficheiro_utilizadores="profiles.txt")

    app = QApplication(sys.argv)
    window = AppWindow(sistema)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
'''''

sistema = SistemaGestaoTarefas(ficheiro_utilizadores="profiles.txt")

app = QApplication(sys.argv)
window = AppWindow(sistema)
window.show()
sys.exit(app.exec_())
'''