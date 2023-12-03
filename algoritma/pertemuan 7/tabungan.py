saldo = float(input('Saldo Awal : Rp. '))
bunga = float(input('Bunga (%) : '))
waktu = int(input('Jangka Waktu : '))
print('-'*50)

for bulan in range(1,waktu+1):
    saldo = saldo + (bunga/100 * saldo)
    print(f'Saldo bulan ke {bulan} : Rp. {saldo:10.0f}')