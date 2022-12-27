# Argumentos nomeados tem nome com sinal de igual
# Arguemtos posicionais recebem apenas o valor.

def soma(x, y):
	print(f'{x=} {y=} -> x + y = {x + y}')

# argumentos posicionais
soma(1, 2) # x=1 y=2 -> x + y = 3

# argumetos nomeados
soma(y=2, x=1) # x=1 y=2 -> x + y = 3

# ambos
soma(1, y=2) # x=1 y=2 -> x + y = 3

""" sempre que se nomear um argumento, os proximos tambem deverao ser nomeados"""