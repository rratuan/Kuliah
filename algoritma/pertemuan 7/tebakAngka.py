import random

level = 0
gameOver = False

while not gameOver:
    level = level + 1
    print('Level',level,'[1 ..',level*10,']')
    rahasia = random.randint(1, level * 10)
    tebakan = 0
    salah = 0
    while salah < 5 and tebakan != rahasia:
        tebakan = int(input('Tebakan anda : '))
        if tebakan == rahasia:
            print('Tebakan anda benar')
            salah = 0
        elif tebakan < rahasia:
            print('Tebakan anda terlalu kecil')
            salah = salah + 1
        elif tebakan > rahasia:
            print('Tebakan anda terlalu besar')
            salah = salah + 1
    if salah == 5:
        print('Game Over.Anda sudah salah tebak sebanyak 5 kali')
        gameOver = True