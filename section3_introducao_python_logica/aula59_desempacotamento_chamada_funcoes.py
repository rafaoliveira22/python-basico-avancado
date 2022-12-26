string = 'ABCD'
lista = ['Rafael', 'Daniel', 1, 2, 3, 'Oliveira']
tupla = 'python', 'é', 'legal'

print(*lista) # 'Rafael', 'Daniel', 1, 2, 3, 'Oliveira'
print(*string) # A B C D
print(*tupla) # python é legal

salas = [
	['Maria', 'Helena'], # 0
	['João', 'Gabriel', 'Lucas'], # 1
	['Rafael', 'Clara', 'Daniel', (10, 20, 30, 40)] # 2
]

print(*salas, sep='\n')
# ['Maria', 'Helena']
# ['João', 'Gabriel', 'Lucas']
# ['Rafael', 'Clara', 'Daniel', (10, 20, 30, 40)]