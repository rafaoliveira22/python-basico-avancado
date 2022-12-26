print('valor' if True else 'Outro valor') # valor
print('valor' if False else 'Outro valor') # Outro valor
print('valor' if False else 'Outro valor' if False else 'Fim') # Fim

condicao = 10 == 10
variavel = 'Rafael' if condicao else 'Não Rafael'
print(variavel) # Rafael