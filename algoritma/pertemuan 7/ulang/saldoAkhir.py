print(' Menghitung Saldo Akhir sampai Bulan Ke-n '.center(80,'='))

# inputan user
saldoAwal = float(input('Saldo Awal     : '))
bunga = float(input('Bunga [%]      : '))
jangkaWaktu = int(input('Jangka Waktu   : '))
print('-'*80)

# perhitungan saldo akhir
for i in range(1,jangkaWaktu+1):
    saldoAwal = (saldoAwal*(bunga/100)) + saldoAwal
    print(f'Saldo Akhir Bulan ke-{i} : Rp.{saldoAwal:10.0f}')