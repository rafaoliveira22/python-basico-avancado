entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_correta = '1234'

if entrada == 'E' and senha_correta == '1234':
	print('Entrar')
else:
	print('Sair')

# valores considerados falsos no python (falsys)
# 0
# 0.0
# ''
# False
# None

# Avaliação de curto circuito
print(True and False and True) # retorno -> False
print(True and 0 and True) # retorno -> 0