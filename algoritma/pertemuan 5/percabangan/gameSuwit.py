import random

print(' Game Kertas-Batu-Gunting '.center(45,'='))

# komputer memilih
komputer = random.choice(['G','K','B'])
print('Komputer telah memilih.Sekarang giliran Anda!')

# pemain memilih
pemain = input('Pilihan Anda (G/K/B) ? ')

# aturan main
if pemain == 'G':
    if komputer == pemain:
        print(f'Komputer memilih {komputer}.Draw!')
    elif komputer == 'K':
        print(f'Komputer memilih {komputer}.Anda Menang!')
    else:
        print(f'Komputer memilih {komputer}.Komputer Menang!')
elif pemain == 'K':
    if komputer == pemain:
        print(f'Komputer memilih {komputer}.Draw!')
    elif komputer == 'G':
        print(f'Komputer memilih {komputer}.Komputer Menang!')
    else:
        print(f'Komputer memilih {komputer}.Anda Kalah!')
elif pemain == 'B':
    if komputer == pemain:
        print(f'Komputer memilih {komputer}.Draw!')
    elif komputer == 'K':
        print(f'Komputer memilih {komputer}.Komputer Menang!')
    else:
        print(f'Komputer memilih {komputer}.Anda Menang!')
else:
    print('Masukkan salah satu dari G/K/B')

print('=' * 45)