

class Node:
    def __init__(self, matricula, nota):
        self.matricula = matricula
        self.nota = nota
        self.proximo = None
        self.anterior = None

class ListaNotas:
    def __init__(self):
        self.cabeca = None

    def inserir_nota(self, matricula, nota):
        novo_aluno = Node(matricula, nota)

        if self.cabeca is None or matricula < self.cabeca.matricula:
            novo_aluno.proximo = self.cabeca
            if self.cabeca is not None:
                self.cabeca.anterior = novo_aluno
            self.cabeca = novo_aluno
            return

        current = self.cabeca
        while current.proximo is not None and current.proximo.matricula < matricula:
            current = current.proximo

        novo_aluno.proximo = current.proximo
        if current.proximo is not None:
            current.proximo.anterior = novo_aluno
        current.proximo = novo_aluno
        novo_aluno.anterior = current

    def buscar_nota(self, matricula):
        current = self.cabeca

        while current is not None:
            if current.matricula == matricula:
                return current.nota
            current = current.proximo

        return "Matrícula não encontrada"

    def apagar_aluno(self, matricula):
        if self.cabeca is None:
            return

        if self.cabeca.matricula == matricula:
            self.cabeca = self.cabeca.proximo
            if self.cabeca is not None:
                self.cabeca.anterior = None
            return

        current = self.cabeca
        while current.proximo is not None and current.proximo.matricula != matricula:
            current = current.proximo

        if current.proximo is None:
            return

        current.proximo = current.proximo.proximo
        if current.proximo is not None:
            current.proximo.anterior = current

    def imprimir_notas(self):
        current = self.cabeca

        while current is not None:
            print(f"Matrícula: {current.matricula}, Nota: {current.nota}")
            current = current.proximo

lista = ListaNotas()

lista.inserir_nota(99, 8.5)
lista.inserir_nota(23, 7.0)
lista.inserir_nota(14, 9.3)

lista.imprimir_notas()

print("\nNota do aluno com matrícula 14:", lista.buscar_nota(14))

lista.apagar_aluno(14)
print(lista.cabeca.proximo.anterior == lista.cabeca)
print("\nApagar o aluno com matricula 14:")
lista.imprimir_notas()
