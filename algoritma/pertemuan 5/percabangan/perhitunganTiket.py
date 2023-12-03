print(' Tiket Kereta Api 2 '.center(30,'='))

# input jurusan
print('''Kode Kota :
1.Jakarta
2.Yogyakarta
3.Surabaya''')

jurusan = int(input('Pilihan Kota [1/2/3] ? '))

#input kelas  
print('''
Kode Kelas :
1.Ekonomi
2.Bisnis
3.Eksekutif''')

kelas = int(input('Pilihan Kelas [1/2/3] ? '))

# inisialisasi diskon
diskon = 0

# pengecekan jurusan dan kelas
if jurusan == 1:
    jurusan = 'Jakarta'
    if kelas == 1:
        kelas = 'ekonomi'
        harga = 200000
    elif kelas == 2:
        kelas = 'bisnis'
        harga = 400000
    elif kelas == 3:
        kelas = 'eksekutif'
        harga = 700000
    else:
        print('Kelas tidak ditemukan')
elif jurusan == 2:
    jurusan = 'Yogyakarta'
    if kelas == 1:
        kelas = 'ekonomi'
        harga = 200000
        kodeVocher = input('Kode Vocher  : ')
        if kodeVocher == 'PROMO':
            diskon = 0.1
        else:
            diskon = 0
    elif kelas == 2:
        kelas = 'bisnis'
        harga = 500000
    elif kelas == 3:
        kelas = 'eksekutif'
        harga = 800000
    else:
        print('Kelas tidak ditemukan')
elif jurusan == 3:
    jurusan = 'Surabaya'
    if kelas == 1:
        kelas = 'ekonomi'
        harga = 300000
    elif kelas == 2:
        kelas = 'bisnis'
        harga = 600000
    elif kelas == 3:
        kelas = 'eksekutif'
        harga = 900000
        kodeVocher = input('Kode Vocher  : ')
        if kodeVocher == 'PROMO':
            diskon = 0.1
        else:
            diskon = 0
    else:
        print('Kelas tidak ditemukan')
else:
    print('Kota Tidak Ditemukan')

# input banyak tiket
banyakTiket = int(input('Banyak Tiket : '))

# sub total pembayaran
subTotal = harga * banyakTiket

# potongan harga
potonganHarga = subTotal * diskon

#total pembayaran
totalBayar = subTotal - potonganHarga

# output
print('=' * 30)
print(f'''Harga Tiket  : Rp. {harga:8.0f}
Sub Total    : Rp. {subTotal:8.0f}
Diskon       : Rp. {potonganHarga:8.0f}
Total Bayar  : Rp. {totalBayar:8.0f}
''')