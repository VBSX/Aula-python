Preparação antes da aula

- usar python 3.10

- Criando o ambiente virtual https://docs.python.org/pt-br/3/library/venv.html

    python -m venv /caminho/para/novo/ambiente/virtual

- Download da biblioteca de interface visual: pip install PySide6

---

Complementação da aula

- Validando campo idade para aceitar apenas números inteiros

    from PySide6.QtGui import QIntValidator
    idade.setValidator(QIntValidator(0, 120))

- Verificando se os campos foram preenchidos antes de salvar

    if nome.text() and idade.text():
        inserir(nome.text(), int(idade.text()))
        nome.clear()
        idade.clear()
        saida.setText("Registro salvo!")
    else:
        saida.setText("Preencha todos os campos!")


