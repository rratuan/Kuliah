import random

# set kesempatan sebanyak 3 kali dimulai dari kesempatan 1
kesempatan = 1

# masuk ke perulangan
while kesempatan <= 3:
    # komputer memilih
    komputer = random.choice(['G','K','B'])
    # pemain memilih
    pemain = input('Komputer sudah memilih.\nSekarang giliran anda,silahkan masukkan pilihan anda [G/K/B]: ')
    # rules game
    if pemain == komputer:
        print('Draw!')
    elif pemain == 'G':
        if komputer == 'K':
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA MENANG!')
        elif komputer == 'B':
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA KALAH!')
            # kesempatan jadi bertambah sampai habis
            kesempatan = kesempatan + 1
    elif pemain == 'K':
        if komputer == 'G':
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA KALAH!')
            # kesempatan jadi bertambah sampai habis
            kesempatan = kesempatan + 1
        elif komputer == 'B':
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA MENANG!')
    elif pemain == 'B':
        if komputer == 'K':
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA KALAH!')
            # kesempatan jadi bertambah sampai habis
            kesempatan = kesempatan + 1
        elif komputer == 'G':
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA MENANG!')

#ketika kesempatan habis 
print('Game Over!')
