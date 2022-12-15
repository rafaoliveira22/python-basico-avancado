velocidade = 61
local_carro = 99

RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1_limite_inferior = local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_passou_radar_1_limite_superior = local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 = carro_passou_radar_1_limite_inferior and carro_passou_radar_1_limite_superior 

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1: 
	print('A velocidade excedeu o limite do radar 1')

if carro_passou_radar_1:
	print('O carro passou no radar 1')

if carro_multado_radar_1:
	print('Carro multado')