condicao = True
passou_no_if = None

if condicao:
	passou_no_if = True # bandeira
	print('Faça algo')
else:
	print('Não faça algo')

# print('passou_no_if, passou_no_if is None') # is None -> == None
if passou_no_if is None:
	print('Não passou no if')

if passou_no_if is not None:
	print('Passou no if')