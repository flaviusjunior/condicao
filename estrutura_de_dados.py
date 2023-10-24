class ItemLista:
    def __init__(self, matricula, nota, proximo = None):
        self.matricula = matricula
        self.nota = nota
        self.proximo = proximo

class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir_nota(self, matricula, nota):
        novo_item = ItemLista(matricula, nota)
        if self.cabeca is None or matricula < self.cabeca.matricula:
            novo_item.proximo = self.cabeca
            self.cabeca = novo_item
            return self

        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.matricula < matricula:
            atual = atual.proximo

        novo_item.proximo = atual.proximo
        atual.proximo = novo_item 

        return self

    def buscar_nota(self, matricula):
        atual = self.cabeca

        while atual is not None:
            if atual.matricula == matricula:
                return atual.nota
            atual = atual.proximo

    def apagar_nota(self, matricula):
        if self.cabeca is None:
            return self

        if self.cabeca.matricula == matricula:
            self.cabeca = self.cabeca.proximo
            return self

        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.matricula != matricula:
            atual = atual.proximo

        if atual.proximo is None:
            return self

        atual.proximo = atual.proximo.proximo
        return self

    def imprimir_notas(self):
        atual = self.cabeca

        while atual is not None:
            print(f"Matrícula: {atual.matricula}, Nota: {atual.nota}")
            atual = atual.proximo

        return self

lista_alunos = Lista()
lista_alunos.inserir_nota(101, 2).inserir_nota(110, 40).inserir_nota(105, 7)
lista_alunos.inserir_nota(99, 4).inserir_nota(12, 4).inserir_nota(120, 4)
# lista_alunos.imprimir_notas()

# numero_matricula = int(input("Digite o numero da matricula para ver a nota: "))
# nota = lista_alunos.buscar_nota(numero_matricula)
# print(f'\nNota do Aluno {numero_matricula}: {nota}')

lista_alunos.imprimir_notas()
print(f'\nAluno 99 foi removido\n')
lista_alunos.apagar_nota(99).imprimir_notas()

# class Node:
#     def __init__(self, matricula, nota, next):
#         self.matricula = matricula
#         self.nota = nota
#         self.next = next


# class ListaNotas:
#     def __init__(self):
#         self.head = None

#     def inserir_nota(self, matricula, nota):
#         novo_aluno = Node(matricula, nota)

#         if self.head is None or matricula < self.head.matricula:
#             novo_aluno.next = self.head
#             self.head = novo_aluno
#             return

#         current = self.head
#         while current.next is not None and current.next.matricula < matricula:
#             current = current.next

#         novo_aluno.next = current.next
#         current.next = novo_aluno

#     def buscar_nota(self, matricula):
#         current = self.head

#         while current is not None:
#             if current.matricula == matricula:
#                 return current.nota
#             current = current.next

#         return "Matrícula não encontrada"

#     def apagar_aluno(self, matricula):
        # if self.head is None:
        #     return

        # if self.head.matricula == matricula:
        #     self.head = self.head.next
        #     return

        # current = self.head
        # while current.next is not None and current.next.matricula != matricula:
        #     current = current.next

        # if current.next is None:
        #     return

        # current.next = current.next.next

#     def imprimir_notas(self):
#         current = self.head

#         while current is not None:
#             print(f"Matrícula: {current.matricula}, Nota: {current.nota}")
#             current = current.next

# # Exemplo de uso:
# lista = ListaNotas()

# lista.inserir_nota(101, 8.5)
# lista.inserir_nota(102, 7.0)
# lista.inserir_nota(103, 9.3)
# lista.inserir_nota(99,10)

# lista.imprimir_notas()

# print("\nNota do aluno com matrícula 102:", lista.buscar_nota(102))

# lista.apagar_aluno(102)

# print("\nApós apagar o aluno com matrícula 102:")
# lista.imprimir_notas()

# print("\nNota do aluno com matrícula 102:", lista.buscar_nota(102))