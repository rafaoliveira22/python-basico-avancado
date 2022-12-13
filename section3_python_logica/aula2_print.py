print(12, 34) # 12 34 (padrão)
print(12, 34, sep = "-") # 12-34

# \r\n -> CRLF (padrão windows)
# \n -> LF (padrão unix)

# \n (padrão)
print(56, 78, sep = "-", end = '\n') 
print(78, 1011, sep = "-", end = '\n')

""" 
saída
56-78
78-1011
"""
 # outros caracteres
print(56, 78, sep = "-", end = '##') 
print(78, 1011, sep = "-")

""" 
saída
56-78##78-1011
"""