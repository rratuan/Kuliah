print(' Perincian Uang Kembalian '.center(42,'='))

# input besar bayar dan total yang harus di bayar
totalBayar = int(input('Total Yang Harus Dibayar : '))
besarBayar = int(input('Besar Bayar              : '))

# proses perhitungan uang kembalian
print('=' * 42)
kembalian = besarBayar - totalBayar
print(f'Kembalian         : {kembalian}')

# proses dan output perincian uang kembalian
print(f'Rincian Kembalian : ')
rincian = kembalian // 50000
print(f'Rp. 50.000 : {rincian} lembar' ) 
kembalian = kembalian % 50000 
# print(kembalian)
rincian = kembalian // 20000
print(f'Rp. 20.000 : {rincian} lembar')
kembalian = kembalian % 20000
# print(kembalian)
rincian = kembalian // 10000
print(f'Rp. 10.000 : {rincian} lembar')
kembalian = kembalian % 10000
# print(kembalian)
rincian = kembalian // 5000
print(f'Rp. 5.000  : {rincian} lembar')
kembalian = kembalian % 5000
# print(kembalian)
rincian = kembalian // 2000
print(f'Rp. 2.000  : {rincian} lembar')
kembalian = kembalian % 2000
# print(kembalian)
rincian = kembalian // 1000
print(f'Rp. 1.000  : {rincian} lembar')
kembalian = kembalian % 1000
# print(kembalian)