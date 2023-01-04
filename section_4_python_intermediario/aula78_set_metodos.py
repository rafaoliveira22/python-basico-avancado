s1 = set()
# add - adicionar valor no set, 1 por vez
s1.add('Rafael')
s1.add(1)
print(s1) # {1, 'Rafael'}

# update - pode mandar vários valores
s1.update(('Olá mundo', 3, 4, 5))
print(s1) # {1, 3, 4, 5,'Olá mundo', 'Rafael'}

# clear - limpa o set
# s1.clear()
# print(s1) # set()

# discard - elimina o valor
s1.discard('Olá mundo')
s1.discard('Rafael')
print(s1) # {1, 3, 4, 5}