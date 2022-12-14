nome = 'Rafael Oliveira'
altura = 1.85
peso = 90
imc = peso / altura ** 2 # ou peso / (altura * altura)

texto = f'{nome}, tem {altura:.2f} de altura\npesa {peso} quilos e seu IMC é {imc:.2f}'
print(texto)