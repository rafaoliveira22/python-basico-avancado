"""
o x ta sendo declarado em um escopo global, ou seja, o mesmo
da função, caso ele tivesse sido declarado dentro da função,
ele estaria em um escopo local e só poderia ser acessado
dentro daquela função.
"""

x = 1
def escopo():
    # global x
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y) # 11 2
    outra_funcao()
    print(x) # 10

escopo()  
print(x) # 1

"""
caso queira manipular o x fora do escopo da funcao, utliza-se a palavra "global" que faz com que uma variavel do escopo externa seja a mesma no escopo interno
x = 1
def escopo():
    global x
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y) # 11 2
    outra_funcao()
    print(x) # 10

print(x) # 1
escopo()  
print(x) # 10
"""