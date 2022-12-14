# Fatiamento [i: f: p] [ : : ]
# i -> inicio f -> final p -> passo (de quantos em quantos caracteres)

# 012345678
# Ola mundo
#-987654321
variavel = 'Ola mundo'
print(variavel[4:8]) # mund -> nesse caso, o indice final não é incluido, ou seja, o 8, entao esta indo do 4 ao 7
print(variavel[4:]) # mundo -> omitindo o final, ele sabe que tem que ir até o final da string
print(variavel[:5]) # Ola m -> omitindo o inicio, ele sabe que tem que começar no inicio da string

# len, retorna a quantidade de caracteres da string
print(len(variavel)) # 9

#
print(variavel[0:len(variavel):1]) # Ola mundo
print(variavel[0:len(variavel):2]) # Oamno
print(variavel[-1:-10:-1]) # odnum alO