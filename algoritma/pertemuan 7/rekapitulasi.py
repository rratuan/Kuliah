data = 0
n = 0
total = 0

while data >= 0:
    n = n + 1
    print(f'Data ke-{n} : ',end='')
    data = int(input())
    if data >= 0:
        total += data
print(f'Total : {total}')
n = n - 1
print(f'Banyak data : {n}')
rataRata = total / n
print(f'Rata-Rata : {rataRata:0.2f}')