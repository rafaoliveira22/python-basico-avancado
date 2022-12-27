def soma(x, y, z=None):
	if z is not None:
		print(f'{x=} {y=} {z=} -> ', x + y + z)
	else:
		print(f'{x=} {y=} -> ', x + y)

soma(1, 2, 3) # 1 2 3 -> 6
soma(4, 5, 0) # 4 5 0 -> 9
soma(1, 2) # 1 2 -> 3

""" 
Todo parametro que vier depois de um parametro com
valor padrão, devera te um valor padrão:
def soma(x, y=None, z=None)
"""
