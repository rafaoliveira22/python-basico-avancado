# 1 - parenteses (n + n)
# 2 - exponenciacao **
# 3 - * / // % (com multiplicação e divisão na mesma conta, a ordem sera da esquerda pra direita)
# 4 - + -

conta_1 = 1 + 1 ** 5 + 5 # 1 ** 5 = 1 -> +1 = 2 -> +5 = 7
conta_2 = (1 + 1) ** (5 + 5) # 1024

print(conta_1)
print(conta_2)