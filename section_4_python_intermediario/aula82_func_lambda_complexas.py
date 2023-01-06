def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


"""
def soma(x, y): -> lambda x, y:
x + y -> return x + y
"""


# soma,  2 params
print(
    executa(lambda x, y: x + y, 2, 3),
    executa(soma, 2, 3),
    soma(2, 3)
)

# cria_multiplicador
duplica = executa(lambda m: lambda n: n*m, 2)
print(duplica(2))

# *args
print(
    executa(
        lambda *args: sum(args), 1, 2, 3,4, 5, 6, 7
    )
)