# exercícios com funções
def multiplicar(*args):
    total = 1
    for i in args:
        total *= i
    return total

print(multiplicar(10, 2, 5, 6))


def verificar_par_impar(num):
    if num % 2 == 0:
        return f'[{num}] -> PAR'
    return f'[{num}] -> ÍMPAR'

print(verificar_par_impar(100))



