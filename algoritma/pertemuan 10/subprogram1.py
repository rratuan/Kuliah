def lingkaran():
    print('Perhitungan luas dan keliling lingkaran')
    radius = float(input('Radius Lingkaran ? '))
    print('Luas Lingkaran :',(3.14 * radius * radius))
    print('Keliling Lingkaran :',(2 * 3.14 * radius))

def persegiPanjang():
    print('Perhitungan luas dan keliling persegi panjang')
    panjang = int(input('Panjang ? '))
    lebar = int(input('Lebar ? '))
    print('Luas Persegi Panjang :',(panjang * lebar))
    print('Keliling Persegi Panjang :',((2*panjang) + (2*lebar)))

def menu():
    print('Aplikasi perhitungan luas dan keliling')
    print('1. Lingkaran\n2. Persegi Panjang\n0. Keluar')
    pilihan = int(input('Pilihan Anda ? '))
    return pilihan

# program utama
pilihan = menu()
if pilihan == 1:
    lingkaran()
elif pilihan == 2:
    persegiPanjang()