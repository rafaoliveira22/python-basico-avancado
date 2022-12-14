# Exercicio

# Peça ao usuário para digitar seu nome
nome = input('Digite seu nome: ')
# Peça ao usuário para digitar sua idade
idade = input('Digite sua idade: ')

# se nome e idade forem digitados, exiba:
if nome and idade:
    # seu nome é {nome}
    print(f'Seu nome é {nome}')
    # seu nome invertido é {nome invertido}
    print(f'Seu nome invertido é {nome[::-1]}')
    # se o nome contem ou nao espacços
    if ' ' in nome: print(f'Seu nome, {nome}, contém espaços')
    else: print(f'Seu nome, {nome}, não contém espaços')
    # seu nome tem {n} letras
    print(f'Seu nome tem {len(nome)} letras')
    # a primeira letra do seu nome é {letra}
    print(f'A primeira letra do seu nome é {nome[0]}')
    # a última letra do seu nome é {letra}
    print(f'A ultima letra do seu nome é {nome[len(nome)-1]}') # ou nome[-1]
# se nada for digitado em nome ou idade:
else:
    print('Desculpe, você deixou campos vazios.')
    