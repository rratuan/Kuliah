import random

komputer = random.choice(['G','K','B'])

print('Komputer telah memilih.Sekarang giliran anda.')
player = input('Pilihan anda [G/K/B] ? ').upper()

if komputer == 'G' and player == 'G':
    print('Draw.')
elif komputer == 'G' and player == 'K':
    print('Anda Kalah.Komputer memilih gunting')
elif komputer == 'G' and player == 'B':
    print('Anda menang.Komputer memilih gunting')
elif komputer == 'K':
    if player == 'G':
        print('Anda menang. Komputer memilih kertas')
    elif player == 'K':
        print('Draw')
    elif player == 'B':
        print('Anda Kalah.Komputer memilih kertas')
elif komputer == 'B':
    if player == 'G':
        print('Anda Kalah.Komputer memilih batu')
    elif player == 'K':
        print('Anda Menang.Komputer memilih batu')
    elif player == 'B':
        print('Draw.')
