import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

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
    segundo_digito = (soma_dez_digitos * 10) % 11

    # Se o resultado anterior for maior que 9: resultado é 0
    # contrário disso: resultado é o valor da conta
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    # print('O SEGUNDO DIGITO DO CPF É: ', segundo_digito)
    cpf_gerado_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(cpf_gerado_calculo)