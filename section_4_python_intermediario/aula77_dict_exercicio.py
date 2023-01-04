# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_acertos = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    print()

    opcoes = pergunta['Opcoes']
    #print(opcoes)
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")

    resposta_user = input('Escolha uma opção: ')

    resposta_user_int = None
    acertou = False
    qtd_opcoes = len(opcoes)

    if resposta_user.isdigit():
        resposta_user_int = int(resposta_user)

    if resposta_user_int is not None:
        if resposta_user_int >= 0 and resposta_user_int < qtd_opcoes:    
            if opcoes[resposta_user_int] == pergunta['Resposta']:
                print('✔ Você acertou')
                qtd_acertos += 1
            else:
                print('❌ Você errou')
    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')