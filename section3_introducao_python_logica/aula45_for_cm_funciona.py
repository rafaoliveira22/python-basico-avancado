# for letra in texto
texto = 'Python' # iterável
iterador = iter(texto) # iterador -> __iter__

print("EXEMPLIFICANDO COMO O FOR FUNCIONA, COM MÉTODOS E WHILE")
while True:
	try:
		letra = next(iterador) # __next__
		print(letra)
	except StopIteration: break

print("UTILIZANDO O FOR")
for letra in texto:
	print(letra)