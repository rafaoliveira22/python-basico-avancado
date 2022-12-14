# 0  1  2  3  4  5 -> índices positivos
# R  a  f  a  e  l
#-6 -5 -4 -3 -2 -1 -> índices negativos

# nome = 'Rafael'
# print(nome[2]) # -> f
# print(nome[-2]) # -> e

# # Nesse caso, o python vai checar letra pro letra para verificar se o 'R' esta entre as letras do nome
# print('R' in nome) # True
# print('y' in nome) # False
# print('afa' in nome) # True
# print('ele' not in nome) # True

nome = input('Digite um nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')