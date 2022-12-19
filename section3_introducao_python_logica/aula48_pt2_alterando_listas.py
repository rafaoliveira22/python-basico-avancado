lista = [10, 215, 30, 700]
print(lista) # [10, 215, 30, 700]

# del -> apaga um item da lista
del lista[2]
print(lista[2]) # 700 (a lista é reorganizada)
print(lista) # [10, 215, 700]

# append -> adiciona ao final da lista
lista.append(50)
lista.append(100)
print(lista) # [10, 215, 700, 50, 100]

# pop -> remove o último elemento da lista
lista.pop()
print(lista) # [10, 215, 700, 50]