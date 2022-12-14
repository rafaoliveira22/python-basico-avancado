"""
s - string
d e i - int
f - float
x(gera um hexa minusculo) e X(gera um hexa maiusculo) - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Rafael'
preco = 1000.928350334
texto_montado = '%s, o preço é R$%.2f' %(nome, preco)
print(texto_montado) # Rafael, o preço é R$1000.92
print('O HEXADECIMAL de %d é %04X' %(5345, 5345)) #ou somente %X, colocando %04X ele preenche o que faltar, ou %08X