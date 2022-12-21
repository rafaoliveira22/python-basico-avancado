nomes = ['Rafael', 'João', 'Luiz']
nomes_enumerados = enumerate(nomes)
print(nomes_enumerados) # <enumerate object at 0x1009fb900>

lista_nomes_enumerados = list(enumerate(nomes))
print(lista_nomes_enumerados) # [(0, 'Rafael'), (1, 'João'), (2, 'Luiz')]

for i in nomes_enumerados:
	print(i) # (0, 'Rafael') (1, 'João')...

print('\nCom desempacotamento -> indice, nome = item')
for item in enumerate(nomes):
	indice, nome = item
	print(f'[{indice}] -> {nome}') # [0] -> Rafael 

# o for acima pode ser simplificado da seguinte forma
print('\ndireto no for -> for i, nome in enumerate(nomes)')
for i, nome in enumerate(nomes):
	print(f'[{i}] -> {nome}') # [0] -> Rafael 