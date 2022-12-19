lista_a = ['Rafael', 'Gabriel']
lista_b = lista_a

"""
isso faz com que as duas variáveis apontem para o mesmo 
endereço de memória. Ou seja, quando eu alterar algo em uma, 
automaticamente ira alterar na outra
"""

lista_a[0] = 'João'
print(lista_b) # ['João', 'Gabriel']

# copy
lista_c = ['Rafael', 'Gabriel', 'João', 'Maria']
lista_d = lista_c.copy()

lista_c[0] = 'Rafinha'
print(lista_c) # ['Rafinha', 'Gabriel', 'João', 'Maria']
print(lista_d) # ['Rafael', 'Gabriel', 'João', 'Maria']