import random

# set kesempatan sebanyak 3 kali 
gameOver = False
kesempatan = 0

# masuk ke perulangan
while not gameOver:
    while kesempatan < 3:
        # komputer memilih
        komputer = random.choice(['G','K','B'])
        # pemain memilih
        pemain = input('Komputer sudah memilih.\nSekarang giliran anda,silahkan masukkan pilihan anda [G/K/B]: ')
        print('-'*30)
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
    # kondisi ketika kesempatan udah abis
    print('-'*30)
    print('Game Over')
    print('-'*30)
    # ketika user ingin bermain lagi
    ulang = input('Mau main lagi [Y/N]? ')
    if ulang == 'Y':
        # set game over agar true
        gameOver = False
        # set ulang kesempatan
        kesempatan = 0
    else:
        print('Terima Kasih sudah bermain!')
        # keluar dari looping
        break
    

