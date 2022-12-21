nomes = ['Rafael', 'João', 'Luiz']
nome1, nome2, nome3 = nomes

print(nome1) # Rafael
print(nome2) # João
print(nome3) # Luiz

# ou
nome1, nome2, nome3 = ['Rafael', 'João', 'Luiz']
print(nome1) # Rafael

# pegando só o 1° valor, para isso, eu preciso indicar o que fazer com o resto
# para isso, o python enpacota o resto, o qual nos indicamos uma variavel com um asterisco
# para indicar que ali é pra ser tratado o resto
nome1, *resto = ['Rafael', 'João', 'Luiz']
print(nome1) # Rafael
print(resto) # ['João', 'Luiz']

""" 
geralmente essa variavel "*resto" não vai ser utilizado
em python, quando uma variável não é utilizada, é aplicada uma convenção
para essa situação, que é utilizar um "_". Isso vai indicar que a variáveç funciona
mas não será utilizada
"""
nome1, *_ = ['Rafael', 'João', 'Luiz']

# se eu quisesse só o 3° valor
_, _, nome3, *_ = ['Rafael', 'João', 'Luiz']
print(nome3) # Luiz