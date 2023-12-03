print(' Tiket Kereta Api 1 '.center(35,'='))

print('''Jurusan :
1.Jakarta
2.Yogyakarta
3.Surabaya''')
# input kota tujuan dan jumlah tiket yang akan dibeli
jurusan = int(input('Pilihan Jurusan [1/2/3] : '))
banyakTiket = int(input('Banyak Tiket            : '))

# proses pemilihan
if jurusan == 1:
    hargaTiket = 150000
elif jurusan == 2:
    hargaTiket = 300000
elif jurusan == 3:
    hargaTiket = 400000
else:
    print('jurusan kota tujuan tidak ditemukan')

# menghitung total bayar
totalBayar = hargaTiket * banyakTiket

# output
print('='*35)
print(f'Harga tiket : Rp. {hargaTiket:7}')
print(f'Total bayar : Rp. {totalBayar}')
