# split
frase = 'Eu estou estudando python, na udemy'
lista_palavras = frase.split() # sem argumento, ele divide nos espaços em branco
print(f'{lista_palavras=}') # ['Eu', 'estou', 'estudando', 'python' ', ',  'na', 'udemy']

# passando argumento
lista_frases = frase.split(', ')
print(f'{lista_frases=}') # ['Eu estou estudando python', 'na udemy']

# strip, rstrip(direita) e lstrip(esquerda)
nome = '    Rafael Oliveira Souza     '
print(nome.strip()) #"Rafael Oliveira Souza"
print(nome.rstrip()) #"     Rafael Oliveira Souza"
print(nome.lstrip()) #"Rafael Oliveira Souza   "  

# join
frases_unidas = '-'.join('abc')
print(frases_unidas) # a-b-c

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)