nome = input('Qual o seu nome? ') # usuário digitou 'Rafael'

print(f'O seu nome é {nome}') # O seu nome é Rafael
print(f'O seu nome é {nome=}') # O seu nome é nome='Rafael'

# números no input
num1 = input('\nDigite um número: ') # 10
num2 = input('Digite outro número: ') # 5
print(f'A soma dos números é (sem conversão): {num1 + num2}') # 105 -> como são duas strs, ele vai concatenar, e não somar

int_num1 = int(num1)
int_num2 = int(num2)
print(f'A soma dos números é: {int_num1 + int_num2}') # 15