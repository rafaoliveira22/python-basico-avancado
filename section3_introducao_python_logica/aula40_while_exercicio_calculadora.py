""" 
Calculdora com while 

- pedir 1° número pro usuário
- pedir 2° númerp pro usuário
- pedir o operador ao usuário
- somente permitir adição, subtração, multiplicação e divisão
- 
"""

while True:
    num1 = input('Digite o 1° número: ')  
    num2 = input('Digite o 2 número: ')  
    op = input('Digite o operador da conta (+-/*): ')  

    numeros_validos = None # flag
    operadores_permitidos = '+-/*' 
    resultado = 0

    num1_float = 0.0
    num2_float = 0.0

    ### VERIFICAR OS NÚMEROS ###
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print(f'Um ou ambos os números digitados -> ("{num1}" "{num2}") é inválido.')
        continue # se um dos números for inválido, volta pra pessoa digitar outro números
    
    ### VERIFICAR OS OPERADORES ###
    if op not in operadores_permitidos or len(op) > 1: 
        print(f'"{op}" -> Operador Inválido')
        continue

    ### EFETUANDO AS CONTAS ###
    if op == '+': 
        resultado = num1_float + num2_float
    elif op == '-': 
        resultado = num1_float - num2_float
    elif op == '/': 
        resultado = num1_float / num2_float
    elif op == '*': 
        resultado = num1_float * num2_float
    else: 
        print('nunca deveria chegar aqui, ta tudo validado')

    ### EXIBINDO O RESULTADO ###
    print(f'{num1_float} {op} {num2_float} = {resultado:.2f}')

    ### SAIR ###
    sair = input('Deseja sair? [s]im ').lower().startswith('s')

    if sair: break