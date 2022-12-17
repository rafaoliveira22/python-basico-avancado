string = 'rafael'
# não teria como por exemplo, atribuir a posição [3] dessa string, um novo valor
# string[3] = 'ABC' # isso não seria aceito pois a str é um tipo imutável.

# o que daria pra usar, é a concatenação, junto ao fatiamento de string
outra_string = f'{string[:3]}ABC{string[4:]}'

print(string) # Rafael
print(outra_string) # RafABCel

# métodos de string
print(string.capitalize()) # Rafael
print(string.zfill(10))