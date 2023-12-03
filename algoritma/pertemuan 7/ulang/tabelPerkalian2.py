angka = int(input('Mau sampai berapa perkaliannya ? '))

for i in range(1,angka+1):
    for j in range(1,angka+1):
        print(f'{i} x {j} = {i*j}')
    print('-' * 20)
