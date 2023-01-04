# operadores

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(f'{s1=}, {s2=}')

# união | união (union) - Une
uniao = s1 | s2
print(f'{uniao=}')

# intersecção & (interserction) - itens presentes em ambos
intersecao = s1 & s2
print(f'{intersecao=}')

# diferença - itens presentes apenas no set da esquerda
diferenca12 = s1 - s2
print(f'{diferenca12=}')

diferenca21 = s2 - s1
print(f'{diferenca21=}')

# diferença simétrica ^ - itens que não estão em ambos
diferenca_simtetrica = s1 ^ s2
print(f'{diferenca_simtetrica=}')