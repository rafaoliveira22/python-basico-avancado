""" 
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
- INSERIR
- APAGAR
- LISTAR OS VALORES DA SUA LISTA
Não permita que o programa quebre  com erros de índices inexistentes na lista
"""
import os

lista_de_compras = []
menu = ['Inserir', 'Apagar', 'Listar', 'Sair']

while True:
    print('SEJA BEM VINDO. O que deseja fazer? (Escolha um número de acordo com o MENU abaixo)')
    for indice_menu, item_menu in enumerate(menu):
        print(f'[{indice_menu}] -> {item_menu}')

    opcao_user = input('OPÇÃO: ')
    
    os.system('cls')
    if opcao_user == str(len(menu) - 1):
        print('Saindo...Sua lista ficou assim: \n')
        for indice_compra, item_compra in enumerate(lista_de_compras):
            print(indice_compra, item_compra)
        break
    elif opcao_user == '0': # inserir -> append
        # os.system('cls')
        item_inserir = input('Qual item deseja inserir? ')
        lista_de_compras.append(item_inserir)
        print(f'"{item_inserir}" inserido na lista de compras\n')
    elif opcao_user == '1': # apagar -> pop(indice)
        try:
            # os.system('cls')
            for indice_compra, item_compra in enumerate(lista_de_compras):
                print(indice_compra, item_compra)
            item_apagar= input('Qual o índice do item você deseja apagar: ')
            item_apagar = int(item_apagar)
            item_apagado = lista_de_compras.pop(item_apagar)
            print(f'"{item_apagado}" removido da lista de compras\n')
        # TRATAMENTO CASO A PESSAOA DIGITE UM ÍNDICE INEXISTENTE
        except IndexError: 
            print('Esse indice não foi encontrado dentro da sua lista, tente novamente.\n')
            continue
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except Exception:
            print('Erro desconhecido')
    elif opcao_user == '2': # listar ->
        # os.system('cls')
        if lista_de_compras == []:
            print('Nada pra listar...')
        else:
            print('LISTA DE COMPRAS')
            for indice_compra, item_compra in enumerate(lista_de_compras):
                print(indice_compra, item_compra) 
            print('\n')
    else: 
        print('Opção inválida. Escolha umas das opções do menu abaixo.')


