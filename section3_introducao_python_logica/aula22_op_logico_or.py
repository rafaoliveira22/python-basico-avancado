entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_correta = '1234'

if (entrada == 'E' or entrada == 'e') and senha_correta == '1234':
	print('Entrar')
else:
	print('Sair')

# Avaliação de curto circuito
print(True or False or 0) # retorno -> True
print(0 or False or 0.0 or 'r' or True) # retorno -> 'r'