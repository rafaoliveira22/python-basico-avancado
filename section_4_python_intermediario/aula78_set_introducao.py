# criação de um set
s1 = set()
print(s1, type(s1)) # set() <class 'set'>

# passando um iterável, mas que pode nao garantir a ordem
s1 = set('Rafael')
print(s1) # {'f', 'l', 'a', 'R', 'e'}
s1 = {'Luiz', 1, 2, 3}
print(s1) # {2, 1, 'Luiz', 3}