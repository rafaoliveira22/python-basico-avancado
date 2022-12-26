# MANEIRAS DE TER SÓ OS NÚMEROS PARA O CÁLCULO
# 01 - .REPLACE()
cpf_enviado_user = '746.824.890-70'.replace(' ', '').replace('.', '').replace('-', '')

# 02 - EXPRESSÃO REGULAR
import re
# tudo que nao for um numero, substituir para nada
cpf_enviado_user = re.sub(r'[^0-9]','', '746.824.890-70')

# CPFS COMO: 111111111, 999999999 SÃO CONSIDERAODS VÁLIDOS
import sys
entrada_eh_sequencial = cpf_enviado_user == cpf_enviado_user[0] * len(cpf_enviado_user)
if entrada_eh_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

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
segundo_digito = 0 if segundo_digito > 9 else segundo_digito

# print('O SEGUNDO DIGITO DO CPF É: ', segundo_digito)
cpf_gerado_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado_user == cpf_gerado_calculo:
    print(f'{cpf_enviado_user} CPF válido')
else: print(f'{cpf_enviado_user} CPF inválido')