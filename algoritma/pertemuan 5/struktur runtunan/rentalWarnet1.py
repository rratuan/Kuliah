print(' Rental Warnet '.center(40,'='))

# input jam masuk,menit masuk,jam keluar,dan menit keluar
jamMasuk = int(input('Jam masuk    : '))
menitMasuk = int(input('Menit masuk  : '))
jamKeluar = int(input('Jam keluar   : '))
menitKeluar = int(input('Menit keluar : '))

# mengubah jam masuk dan keluar menjadi menit
waktuMasuk = jamMasuk * 60 + menitMasuk
waktuKeluar = jamKeluar * 60 + menitKeluar

# menentukan lama rental
lamaRental = waktuKeluar - waktuMasuk

# mengubah waktu lama rental ke dalam jam dan menit
jamRental = lamaRental // 60
menitRental = lamaRental % 60

# menghitung biaya rental 
biayaRental = (lamaRental / 60) * 5000

# output 
print("=" * 40)
print(f"""Lama rental  : {lamaRental} menit ({jamRental} jam {menitRental} menit)
Biaya rental : Rp. {biayaRental:.0f}
""")

