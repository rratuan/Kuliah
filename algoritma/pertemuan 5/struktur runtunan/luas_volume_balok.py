print(' Perhitungan Balok '.center(30,'='))

# input panjang,lebar,tinggi
panjang = int(input('masukkan panjang balok : '))
lebar = int(input('masukkan lebar balok : '))
tinggi = int(input('masukkan tinggi balok : '))

# proses perhitungan luas dan volume
luasPermukaan = 2*((panjang*lebar) + (panjang*tinggi) + (lebar*tinggi))
volume = panjang*lebar*tinggi

print('='*30)
# output luas permukaan,volume,dan dimensi
print (f'luas permukaan balok : {luasPermukaan}')
print (f'volume balok : {volume}')
print(f'dimensi balok : {panjang} x {lebar} x {tinggi}')
