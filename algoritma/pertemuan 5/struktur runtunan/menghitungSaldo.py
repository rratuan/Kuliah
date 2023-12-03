print(' Menghitung Saldo Akhir '.center(40,'='))

# inputkan saldo awal,bunga dan jangka waktu
saldoAwal = int(input('Saldo Awal     : '))
bunga = int(input('Bunga (%)      : '))
jangkaWaktu = int(input('Jangka Waktu   : '))

# menghitung saldo akhir
saldoAkhir = saldoAwal * (1 + (bunga/100))**jangkaWaktu

# output saldo akhir
print('=' * 40)
print(f'Saldo Akhir    : Rp. {saldoAkhir:.2f}')