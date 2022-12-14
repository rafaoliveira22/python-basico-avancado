print(1 + 1) # 2
print('oi' + ' Rafael') # oi Rafael

# print('1' + 1) ->  erro de tipos, pois nao se pode concaternar str com int, somente str com str

# str -> int
int('1') # -> 1
print(int('1') + 1) # 2

# str -> float
float('1') # -> 1.0
print(float('1') + 1) # 2.0

# str -> bool
print(bool('')) # -> False -> str vazia é considerada False
print(bool(' ')) # -> True -> str com conteúdo é considerada True

# int -> str
str(11) # -> '11'
print(str(11) + 'b') # 11b