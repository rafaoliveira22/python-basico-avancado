# Exercicios
# Crie funções que duplicam, triplicam e 
# quadriplicam o número recebido como parametro

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# print(duplicar(2)) # 4
# print(triplicar(2)) # 6
# print(quadruplicar(2)) # 8

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

# deixa-se o retorno apenas com o nome da função
# para possibilitar que a pessoa que va usar
# utilize como querer, por exemplo, duplicando, triplicando e assim sucessiavamente

duplicar = criar_multiplicador(2)
print(duplicar(2)) # 2(numero) * 2(multiplicador)

triplicar = criar_multiplicador(3)
print(triplicar(2))

quadruplicar = criar_multiplicador(4)
print(quadruplicar(2))
