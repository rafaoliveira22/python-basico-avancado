numero_str = input('Vou dobrar o número que você digitar: ')

try:
	print('STR: ', numero_str)
	numero_float = float(numero_str)
	print('FLOAT: ', numero_float)
	print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
	print('Isso não é um número')

# no except tambem é possivel capturar o erro que ocorreu
# isso faz com que o 1° ocorra que ocorra ja gere uma exceção, alterando o fluxo do código, fazendo com o que o erro seja tratado,ou identificado o mais rapido possivel