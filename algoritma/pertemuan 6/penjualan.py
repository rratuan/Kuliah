kode_barang = input('Kode Barang : ').upper()
qty = int(input('Qty         : '))
print('-' * 30)

if kode_barang == 'BK001':
    nama_barang = 'Buku Tulis'
    harga = 5000
elif kode_barang == 'PS002':
    nama_barang = 'Pensil'
    harga = 2500
elif kode_barang == 'PG001':
    nama_barang = 'Penggaris 30 cm'
    harga = 15000
else:
    nama_barang = 'Tidak Dikenal'
    harga = 0

print(f'Nama Barang : {nama_barang}')
print(f'Harga       : Rp. {harga:10}')

subtotal = harga * qty
diskon = 0.30 * subtotal
if diskon > 20000:
    diskon = 20000

total = subtotal - diskon
print(f'Sub Total   : Rp. {subtotal:10}')
print(f'Diskon      : Rp. {diskon:10.0f}')
print(f'Total       : Rp  {total:10.0f}')