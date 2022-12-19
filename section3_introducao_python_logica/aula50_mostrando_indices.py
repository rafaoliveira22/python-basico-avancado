lista = ['Rafael', 'Gabriel', 'João']
indice = 0

for i in lista:
    print(f'[{indice}] -> {i}')
    indice += 1 

# outro jeito
indices = range(len(lista))
print(indices) # range(0,3)

for indice in indices:
    print(indice, lista[indice])
