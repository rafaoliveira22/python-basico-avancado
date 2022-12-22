# 
num_1 = 0.1
num_2 = 0.7
soma = num_1 + num_2
print('SOMA DE FLOAT', soma) # 0.79999999
print(f'{soma:.2f}') # 0.80

# round()
print('SOMA DE FLOAT COM O ROUND', round(soma, 2)) # 0.8

# decimal
import decimal

num_1 = decimal.Decimal('0.1')
num_2 = decimal.Decimal('0.7')
soma = num_1 + num_2
print('SOMA DE FLOAT COM O MÓDULO DECIMAL', soma) # 0.80