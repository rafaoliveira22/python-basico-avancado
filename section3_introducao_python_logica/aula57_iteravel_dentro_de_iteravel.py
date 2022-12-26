salas = [
	['Maria', 'Helena'], # 0
	['João', 'Gabriel', 'Lucas'], # 1
	['Rafael', 'Clara', 'Daniel', (10, 20, 30, 40)] # 2
]

print(salas) # [['Maria', 'Helena'], ['João', 'Gabriel', 'Lucas'], ['Rafael', 'Clara', 'Daniel']]
print(salas[2]) # ['Rafael', 'Clara', 'Daniel', (10, 20, 30, 40)]
print(salas[0][1]) # Helena
print(salas[2][2]) # Daniel
print(salas[2][3][1]) # 20

# utilizando for
print('\n\nUTILZANDO O FOR')
for sala in salas:
	print(f'A sala é {sala}')
	for aluno in sala:
		print(aluno)