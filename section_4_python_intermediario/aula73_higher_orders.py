def saudacao(msg, nome):
	return f'{msg}, {nome}!'

def executa(funcao, *args):
	return funcao(*args)


print(executa(saudacao, 'Olá', 'Rafael')) # Olá, Rafael!
print(executa(saudacao, 'Bom dia', 'Maria')) # Bom dia, Maria!