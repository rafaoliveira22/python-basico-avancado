pessoa = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira'
}

a,b = pessoa # desempacotamento de chaves
print(a, b) # nome sobrenome

a, b = pessoa.values() # desempacotamento de valores
print(a, b) # Rafael Oliveira

a, b = pessoa.items() # desempacotamento de chave/valor
print(a, b) # ('nome', 'Rafael') ('sobrenome', 'Oliveira')

(a1, a2), (b1, b2) = pessoa.items() # desempacotamento interno
print(a1, a2) # nome Rafael
print(b1, b2) # sobrenome Oliveira

# juntanto dicts (desempacotamento de dicionarios)
print()
pessoa = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira'
}

dados_pessoa = {
	'idade': 18,
	'altura': 1.85
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa) # {'nome': 'Rafael', 'sobrenome': 'Oliveira', 'idade': 18, 'altura': 1.85}

# kwargs
print()
# empacotando os argumentos no kwargs
def mostro_argumentos_nomeados(*args, **kwargs):
	print('Não nomeados: ',  args)	

	for chave, valor in kwargs.items():
		print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Rafael', qlq=123)
# Não nomeados: (1, 2)
# nome Rafael
# qlq 123

mostro_argumentos_nomeados(**pessoa_completa)
""" 
Não nomeados: ()
nome Rafael
sobrenome Oliveira
idade 18
altura 1.85
"""