frase = 'O são paulo futebol clube é o maior time do Brasilaaaaaa'

i = 0
letra_mais_repetida = frase[0]
letra_atual= frase[0]

while i < len(frase):
    letra_atual = frase[i]
    i += 1

    # desconsiderar os espaços em branco
    if letra_atual == ' ': continue

    count_letra_atual = frase.count(letra_atual)
    count_letra_mais_repetida = frase.count(letra_mais_repetida)
    if  count_letra_atual > count_letra_mais_repetida:
        letra_mais_repetida = letra_atual
    
print(f'A letra que mais apareceu foi: "{letra_mais_repetida}" com {count_letra_mais_repetida}X')




