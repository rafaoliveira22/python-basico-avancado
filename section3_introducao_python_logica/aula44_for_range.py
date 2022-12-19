""" 
range(start, stop, step)
start - digito inicial
stop - digito final (o ultimo digito não é incluido)
step - pula de quantos em quantos

quando se passa apenas um argumento -> range(10), esse 10 é considerado
o 'stop', o start é 0 e o step 1.
"""

numeros = range(0, 10, 2) 

for numero in numeros:
	print(numero) # 0 2 4 6 8 -> o ultimo numero não é incluido, 0-9