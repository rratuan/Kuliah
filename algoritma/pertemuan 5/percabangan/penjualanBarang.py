print(' Penjualan Barang '.center(30,'='))

# input kode barang dan kuantitas
kodeBarang = input('Kode Barang : ')
qty = int(input('Qty         : '))

# pengecekan barang
if kodeBarang.upper() == 'BK001':
    namaBarang = 'Buku Tulis'
    harga = 5000
elif kodeBarang.upper() == 'PS002':
    namaBarang = 'Pensil'
    harga = 2500
elif kodeBarang.upper() == 'PG001':
    namaBarang = 'Penggaris 30 cm'
    harga = 15000
else:
    namaBarang = 'Barang Tidak Ditemukan!'
    harga = 0

# perhitungan sub total
subTotal = harga * qty

# penentuan diskon
diskon = 0.30 * subTotal
if diskon > 20000:
    diskon = 20000

# menghitung total bayar
total = subTotal - diskon

# output
print('='*30)
print(f'''Nama Barang : {namaBarang}
Harga       : Rp. {harga:6.0f}
Sub Total   : Rp. {subTotal:6.0f}
Diskon      : Rp. {diskon:6.0f}
Total Bayar : Rp. {total:6.0f}
''')