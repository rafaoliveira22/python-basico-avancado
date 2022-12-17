# while e else, quando o laço é executado completamente, o else é executado

nome = 'Rafael'
i = 0

while i < len(nome):
    letra = nome[i]
    if letra == '': break
    print(letra)
    i += 1
else:
    print('Não encontrei nenhum espaço no nome')