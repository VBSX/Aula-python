from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from database import criar_tabela, inserir, consultar
# from PySide6.QtGui import QIntValidator

criar_tabela()

def salvar():
    # if nome.text() and idade.text():
    inserir(nome.text(), idade.text())
    nome.clear()
    idade.clear()
    saida.setText("Registro salvo!")
    # else:
    #     saida.setText("Preencha todos os campos!")
    
def mostrar():
    registros = consultar()
    texto = "\n".join([f"{r[0]} - {r[1]} ({r[2]} anos)" for r in registros])
    saida.setText(texto)

app = QApplication([])

janela = QWidget()
janela.setWindowTitle("Cadastro de Pessoas")

layout = QVBoxLayout()

nome = QLineEdit()
nome.setPlaceholderText("Nome")

idade = QLineEdit()
idade.setPlaceholderText("Idade")
# idade.setValidator(QIntValidator(0, 120))

botao_salvar = QPushButton("Salvar")
botao_consultar = QPushButton("Consultar")

botao_salvar.clicked.connect(salvar)
botao_consultar.clicked.connect(mostrar)

saida = QTextEdit()
saida.setReadOnly(True)

layout.addWidget(nome)
layout.addWidget(idade)
layout.addWidget(botao_salvar)
layout.addWidget(botao_consultar)
layout.addWidget(saida)

janela.setLayout(layout)
janela.show()

app.exec()






