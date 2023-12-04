import random

# set kondisi awal,level,dan kesempatan salah
gameStart = True
level = 0
salah = 0

# masuk ke perulangan
while gameStart:
    level += 1
    komputer = random.randint(1,level*10)

    print('-'*66)
    print('| Anda diberi 5 kali kesempatan menjawab salah di setiap levelnya |')
    print('-'*66)
    print(f'Level {level},Tebak dari [1...{level*10}]')
    
    # rule game
    while salah < 5:
        pemain = int(input('Tebakan Anda ? '))
        if pemain > komputer:
            print('Salah.Tebakan anda Terlalu Besar')
            # salah bertambah
            salah += 1
        elif pemain < komputer:
            print('Salah.Tebakan anda Terlalu Kecil')
            # salah bertambah
            salah += 1
        else:
            print('Selamat.Tebakan Anda Benar')
            # set ulang salah untuk next level
            salah = 0
            break
    
    # kondisi ketika sudah salah 5 kali
    if salah == 5:
        print(f'Game Over.Anda telah salah menebak sebanyak {salah} kali')
        print(f'Angka Rahasia adalah {komputer}')
        gameStart = False
