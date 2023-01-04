# dict
pessoa = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira',
	'idade': 18,
	'altura': 1.85,
	'endereços':[
		{'rua': 'tal', 'numero': 254},
		{'rua': 'outro tal', 'numero': 325}
	] # lista enderecos
} # dict pessoas

# ou pessoa = dict(nome='Rafael', sobrenome='Oliveira'...)

# acessando um valor
print(pessoa['nome']) # Rafael

# em um for, o python retorna as chaves de um dict
for chave in pessoa:
	print(chave, pessoa[chave]) # nome Rafael...