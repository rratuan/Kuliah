data = 0
total = 0
n = 0

while data >= 0:
    n = n + 1
    data = int(input(f'Masukkan Data ke-{n} : '))
    # data yang bernilai negatif akan otomatis keluar dari loop
    if data >= 0:
        total = total + data

print ('-'*30)
print(f'Total       : {total}')

n = n - 1
print(f'Banyak Data : {n}')

print(f'Rata-Rata   : {total/n:0.2f}')
