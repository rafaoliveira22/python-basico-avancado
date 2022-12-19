lista = [10, 215, 30, 700]
lista.insert(0, 400) # 0 -> o índice que vai ser adicionado, 400 -> o valor que vai ser adicionado

print(lista) # [400, 10, 215, 30, 700]

# se um índice maior que a lista for passado, ele adiciona o valor no final da lista
lista.insert(1000, 5)
print(lista) # [400, 10, 215, 30, 700, 5]

# clear -> limpa a lista
lista.clear()
print(lista) # []