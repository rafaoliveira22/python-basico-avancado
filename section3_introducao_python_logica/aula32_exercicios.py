""" 
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um numero inteiro. 
"""
print(F'{"=" * 5} EXERCÍCIO 01 {"=" * 5}')
num = input('Digite um número: ')

# ou if num.isdigit()
try:
    num_int = int(num)
    num_par_impar = num_int % 2 == 0
    par_impar_saida_texto = 'ÍMPAR'

    if num_par_impar: 
        par_impar_saida_texto = 'PAR'
    print(f'{num_int} -> {par_impar_saida_texto}')
except:
    print('Isso não é um número inteiro')
print(F'{"=" * 24}\n')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa Tarde 12-17 e Boa Noite 18-23
"""
print(f'{"=" * 5} EXERCÍCIO 02 {"=" * 5}')
horario_user = input('Digite o horário em número inteiros: ')
try:
    horario_user = int(horario_user)

    dia = horario_user >= 0 and horario_user <= 11 
    tarde = horario_user >= 12 and horario_user <= 17 
    noite = horario_user >= 18 and horario_user <= 23

    if dia: print('Bom dia') 
    elif tarde: print('Boa Tarde') 
    elif noite: print('Boa Noite') 
    else: print('Não conheço essa hora')

except:
    print('Esse horário não é valida como número inteiro')
print(f'{"=" * 24}\n')

"""
Faça um programa que peça o primeiro nome do usuário. 
- Se o nome tiver 4 letras ou menos escreva 'Seu nome é curto'; 
- Se tiver entre 5 e 6 letras, escreva 'Seu nome é normal'; 
- maior que 6 escreva 'Seu nome é muito grande'
"""

print(f'{"=" * 5} EXERCÍCIO 03 {"=" * 5}')

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)
classificacao_nome = ''

if tamanho_nome > 1:
    if tamanho_nome <= 4: classificacao_nome = 'curto'
    elif tamanho_nome <= 6: classificacao_nome = 'normal'
    elif tamanho_nome > 6: classificacao_nome = 'grande'
else: print('Digite mais de 1 letra')

print(f'Seu nome é {classificacao_nome}')

print(f'{"=" * 24}\n')