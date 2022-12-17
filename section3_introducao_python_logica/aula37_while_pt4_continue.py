i = 0
while i < 100:
    i += 1  # i = i + 1

    if i == 6: 
        print('Nâo vou mostrar o 5+1 kakakak')
        continue # 1 2 3 4 5 7 8 9... 40 Acabou o while, i = 40
    print(i)
    if i == 40: 
        break

print(f'Acabou o while, {i=}')