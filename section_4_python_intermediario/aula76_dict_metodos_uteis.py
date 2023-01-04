pessoa = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira'
}

# len - quantas chaves
print(len(pessoa)) # pessoa.__len__ -> 2

# keys - iterável com as chaves
print(pessoa.keys()) # dict_keys(['nome', 'sobrenome'])
"""Para utilizar esses valores retornados, basta fazer
uma coersão para lista, ou tupla.
list(pessoa.keys())
tuple(pessoa.keys())
"""

for chave in pessoa.keys():
	print(chave) # nome sobrenome

# values - iterável com os valores
print(list(pessoa.values())) # ['Rafael', 'Oliveira']
for valor in pessoa.values():
	print(valor) # Rafael Oliveira

# items - iterável com chaves e valores
print(list(pessoa.items())) # [('nome', 'Rafael'), ('sobrenome', 'Oliveira')]
for chave, valor in pessoa.items():
	print(chave, valor) # nome Rafael sobrenome Oliveira

# setdefault - adiciona valor se a chave não existe
pessoa.setdefault('idade', 0)
print(pessoa['idade']) # 0

# copy - retorna uma cópia rasa (shallow copy)
d1 = {
	'c1': 1,
	'c2': 2,
	'l1': [0, 1, 2],
}

""" tudo que for imutável será copiado pra d2,
ou seja, o c1 e o c2. Os dados mutáveis,  nesse caso o l1, sera
linkado com o d1, ou seja, o que for alterado em l1 na d2
sera alterado na d1 automaticamente, e vice versa.
Ambos os dicts, apontam a lista para o mesmo endereço de memória
"""
d2 = d1.copy()
print(d2) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
d2['c1'] = 10
d2['l1'][1] = 27

print(f'{d1=}') # {'c1': 1, 'c2': 2, 'l1': [0, 27, 2]}
print(f'{d2=}') # {'c1': 10, 'c2': 2, 'l1': [0, 27, 2]}

# módulo copy para copiar realmente todos os tipos de dados (deep copy)
import copy
d1 = {
	'c1': 1,
	'c2': 2,
	'l1': [0, 1, 2],
}
d2 = copy.deepcopy(d1)
d2['c1'] = 10
d2['l1'][1] = 27

print(f'{d1=}') # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
print(f'{d2=}') # {'c1': 10, 'c2': 2, 'l1': [0, 27, 2]}

# get - obtém uma chave
p1 = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira'
}
print(p1.get('nome')) # Rafael
del p1['nome']
print(p1.get('nome')) # None
print(p1.get('nome', 'Nome não existe')) # Nome não existe

# pop - apaga o item com a chave especificada (del)
p1 = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira'
}
nome = p1.pop('nome') # remove o item e retorna ele
print(nome) # Rafael
print(p1) # {'sobrenome': 'Oliveira'}

# popitem - apaga o último item adicionado
p1 = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira'
}
ultima_chave = p1.popitem() # remove o ultimo item e retorna ele
print(ultima_chave) # {'sobrenome': 'Oliveira'}
print(p1) # {'nome': 'Rafael'}

# update - atualiza um dicionário com outro
p1 = {
	'nome': 'Rafael',
	'sobrenome': 'Oliveira'
}
# 1° jeito
p1.update({
	'nome': 'novo nome', # atualizando
	'idade': 18, # criando

})
print(p1) # {'nome': 'novo nome', 'sobrenome': 'Oliveira', 'idade': 18}

# 2° jeito - argumentos nomeados
p1.update(nome='novo nome arg nomeado', idade=19)
print(p1) # {'nome': 'novo nome arg nomeado', 'sobrenome': 'Oliveira', 'idade': 19}

# 3° jeito - tupla
tupla= ('nome', 'Rafael'), ('idade', 22)
lista= ['nome', 'Rafael'], ['idade', 22]
p1.update(tupla)
print(p1) # {'nome': 'Rafael', 'sobrenome': 'Oliveira', 'idade': 22}
