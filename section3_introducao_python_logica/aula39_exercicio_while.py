"""
Iterando strings com while
"""

nome = 'Rafael Oliveira'
novo_nome = ''
i = 0

while i < len(nome):
    # print(f'[{i}] -> {nome[i]}')
    # novo += f'*{nome[i]}'
    novo_nome += '*' + nome[i]
    i += 1

novo_nome += '*' # pra aparacer um * no final
print(novo_nome) # *R*a*f*a*e*l* *O*l*i*v*e*i*r*a*

