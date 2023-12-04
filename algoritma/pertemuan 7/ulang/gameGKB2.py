import random

# set kesempatan sebanyak 3 kali 
gameOver = False
kesempatan = 0

# set score awal
scorePemain = 0
scoreKomputer = 0

# masuk ke perulangan
while not gameOver:
    print('-'*50)
    print('| Anda Dikasih Kesempatan Sebanyak 3 Kali Kalah |')
    print('-'*50)
    
    while kesempatan < 3:
        # komputer memilih
        komputer = random.choice(['G','K','B'])
        # pemain memilih
        pemain = input('Komputer sudah memilih.\nSekarang giliran anda,silahkan masukkan pilihan anda [G/K/B]: ').upper()
        print('-'*50)
        # rules game
        if pemain == komputer:
            print('Draw!')
        elif (pemain == 'G' and komputer == 'K') or (pemain == 'K' and komputer == 'B') or (pemain == 'B' and komputer == 'G'):
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA MENANG!')
            # score bertambah
            scorePemain += 1
        else:
            print(f'Komputer memilih {komputer} dan anda memilih {pemain},jadi ANDA KALAH!')
            # kesempatan jadi bertambah sampai habis
            kesempatan += 1
            print(f'Kesempatan anda : {kesempatan}')
            # score bertambah
            scoreKomputer += 1

    # perhitungan score
    if scorePemain == scoreKomputer:
        hasil = 'Draw'
    elif scorePemain > scoreKomputer:
        hasil = 'Selamat,Game ini dimenangkan oleh Anda!'
    else:
        hasil = 'Maaf,Anda Kalah dalam Game kali ini!'

    # kondisi ketika kesempatan udah abis
    print('-'*50)
    print('Game Over')
    print(f'Dengan Score {scorePemain} : {scoreKomputer}')
    print(hasil)
    print('-'*50)
    
    # ketika user ingin bermain lagi
    ulang = input('Mau main lagi [Y/N]? ').upper()
    if ulang == 'Y':
        # set game over agar true
        gameOver = False
        # set ulang kesempatan
        kesempatan = 0
        # set ulang score
        scorePemain = 0
        scoreKomputer = 0
    else:
        print(' Terima Kasih sudah bermain! '.center(50,'-'))
        # keluar dari looping
        break
    

