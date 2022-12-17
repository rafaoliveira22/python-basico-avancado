condicao = True

while condicao:
	nome = input('Qual o seu nome: ')
	print(f'Seu nome é {nome}')

	if nome == 'sair':
		break # faz sair do laço