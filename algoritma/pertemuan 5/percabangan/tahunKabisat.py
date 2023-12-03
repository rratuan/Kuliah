print(' Menentukan Tahun Kabisat '.center(40,'='))

# input tahun
tahun = int(input('Tahun : '))

# pengecekan tahun kabisat dan output
if tahun%100 == 0 and tahun%400 == 0:
    print(f'Tahun {tahun} adalah tahun kabisat')
elif tahun%4 == 0 and tahun%100 != 0:
    print(f'Tahun {tahun} adalah tahun kabisat')
else:
    print(f'Tahun {tahun} bukan tahun kabisat')