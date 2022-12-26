"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

cpf_enviado_user = '74682489070'

# (fatiamento) noves primeiros digitos
nove_digitos = cpf_enviado_user[:9]

# multiplicando cada um dos valores por uma contagem regressiva começando de 10
count_regressivo_digito_1 = 10
soma_nove_digitos = 0

for digito in nove_digitos:
    # Somar todos os resultados
    soma_nove_digitos += int(digito) * count_regressivo_digito_1
    count_regressivo_digito_1 -= 1

# Multiplicar o resultado anterior por 10
# Obter o resto da divisão da conta anterior por 11
primeiro_digito = (soma_nove_digitos * 10) % 11

# Se o resultado anterior for maior que 9: resultado é 0
# contrário disso: resultado é o valor da conta
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
# print('O PRIMEIRO DIGITO DO CPF É: ', primeiro_digito)

# soma dos 9 primeiros dígitos do CPF
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 10
dez_digitos = nove_digitos + str(primeiro_digito)
count_regressivo_digito_2 = 11
soma_dez_digitos = 0

for digito in dez_digitos:
    soma_dez_digitos += int(digito) * count_regressivo_digito_2
    count_regressivo_digito_2 -= 1

# Multiplicar o resultado anterior por 10
# Obter o resto da divisão da conta anterior por 11
segundo_digito = (soma_dez_digitos) % 11

# Se o resultado anterior for maior que 9: resultado é 0
# contrário disso: resultado é o valor da conta
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

# print('O SEGUNDO DIGITO DO CPF É: ', segundo_digito)
cpf_gerado_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado_user == cpf_gerado_calculo:
    print(f'{cpf_enviado_user} CPF válido')
else: print(f'{cpf_enviado_user} CPF inválido')

