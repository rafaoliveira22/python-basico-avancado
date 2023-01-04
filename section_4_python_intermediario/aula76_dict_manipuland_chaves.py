# criando chave
pessoa = {}
pessoa['nome'] = 'Rafael'
print(pessoa) # {'nome': 'Rafael'}

# criando chave dinamica
pessoa = {}
chave = 'nome_completo'
pessoa[chave] = 'Rafael Oliveira'
print(pessoa[chave]) # Rafael Oliveira
print(pessoa) # {'nome_completo': 'Rafael Oliveira'}

# alterando o valor
pessoa = {}
chave = 'nome'
pessoa[chave] = 'Rafael'
print(pessoa[chave]) # Rafael
print(pessoa) # {'nome': 'Rafael'}

pessoa[chave] = 'Joao'
print(pessoa[chave]) # Joao
print(pessoa) # {'nome': 'Joao'}

# apagando
pessoa = {}
chave = 'nome'
pessoa[chave] = 'Rafael'
pessoa['sobrenome'] = 'Oliveira'
print(pessoa) # {'nome': 'Rafael', 'sobrenome': 'Oliveira'}
del pessoa['sobrenome']
print(pessoa) # {'nome': 'Rafael'}

# tratando excecção
pessoa = {}
chave = 'nome'
pessoa[chave] = 'Rafael'
pessoa['sobrenome'] = 'Oliveira'
print(pessoa) # {'nome': 'Rafael', 'sobrenome': 'Oliveira'}
del pessoa['sobrenome']
"""
print(pessoa['sobrenome'] # KeyError
Isso irá gerara uma exceção, nesse caso, uma KeyError
pois a chave 'sobrenome' foi deletada
"""
print(pessoa.get('sobrenome')) # None

# Tratando a exceção
if pessoa.get('sobrenome') is None:
	print('não existe')
else:
	print(f"existe, {pessoa['sobrenome']}")