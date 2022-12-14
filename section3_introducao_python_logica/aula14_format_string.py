a = 'A'
b = 'B'
c = 1.1

formato = 'a = {} b = {} c = {:.2f}'.format(a, b, c) 
print(formato) # -> a = A b = B c = 1.10
# a,b e c são argumentos
# seguindo a ordem, dentro da primeira chave (a = {}) vai vir o 
# primeiro argumento passado em format(), que no caso, é o a.

# ou
string = 'a = {} b = {} c = {:.3f}'
formato = string.format(a, b, c)
print(formato) # -> a = A b = B c = 1.100

# utilizando os índices
string = 'a = {0} a = {0} a = {0} b = {1} c = {2}'
formato = string.format(a, b, c)
print(formato) # -> a = A a = A a = A b = B c = 1.1

# erro
# string = '\na = {} b = {} c = {} {}'
# formato = string.formato(a, b, c)
# daria um erro de "index out of range", pois esta buscando algo que já acabou
# foram passadas 4 chaves (a = {} b = {} c = {} {}), para 3 argumentos (a, b, c), a ultima chave, ficaria sem argumento


# utilizando parametros nomeados
string = 'a = {nome1} b = {nome2} c = {nome3}'
formato = string.format(nome1 = a, nome2 = b, nome3 = c)
print(formato) # -> a = A b = B c = 1.1