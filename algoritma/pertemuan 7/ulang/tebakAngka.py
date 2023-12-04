import random

komputer = random.randint(1,10)
print(komputer)
gameStart = True

while gameStart:
    tebak = int(input('Tebakan anda [1..10] ? '))
    if tebak > komputer:
        print('Salah.Tebakan anda Terlalu Besar')
    elif tebak < komputer:
        print('Salah.Tebakan anda Terlalu Kecil')
    else:
        print('Selamat.Tebakan Anda Benar')
        gameStart = False
