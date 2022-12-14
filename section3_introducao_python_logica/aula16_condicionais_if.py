entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
	print('Você entrou no sistema')
elif entrada == 'sair':
	print('Você saiu do sistema')
else:
	print(f'A opção "{entrada}" é inválida. Digite "entrar" ou "sair".')

print('FORA DOS BLOCOS')
