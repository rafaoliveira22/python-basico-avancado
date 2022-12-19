lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# + -> concatena duas listas
lista_c = lista_a + lista_b
print(f'Concantenação: {lista_c=}') # [1, 2, 3, 4, 5, 6]


"""
.extend()

lista_d = lista_a.extend(lista_b)
print(lista_d) # None

O método extend() não retorna nada, ou seja, ele trabalha em cima
do proprio elemento que esta chamando, nesse caso a lista_a. Ou seja,
não tem como pegar o "lista_a.extend(lista_b)" e jogar em uma variável.
"""

lista_a.extend(lista_b)
print(f'Estendendo: {lista_a=}') # [1, 2, 3, 4, 5, 6]