# desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto) # 1 2 [3, 4]

def soma(*args):
	total = 0
	for i in args:
		total += i
	return total

# tudo que for passado de argumento,vai ser empacotado em args
soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3) # 6

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6) # 15

outra_soma = soma(11,3242,532,6)
print(outra_soma) # 3791

# para enviar uma tupla para função, basta desempactola
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma(*numeros)
print(outra_soma) # 45
