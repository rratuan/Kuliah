i = 1
hasil_kuadrat = 0
hasil_jumlah = 0

while i <= 1000:
    hasil_kuadrat = i**2
    hasil_jumlah = hasil_jumlah + hasil_kuadrat 
    if i == 1000:
        print(hasil_kuadrat,'=',hasil_jumlah)
    else:
        print(hasil_kuadrat,'+',end=' ')
    i = i + 1
    