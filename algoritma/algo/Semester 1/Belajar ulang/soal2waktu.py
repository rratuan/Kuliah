#I.S. Pengguna memasukkan Waktu lari Jam, Menit, Detik
#F.S. Menampilkan hasil waktu dalam satuan detik

hh = int(input("Masukkan hh : " ))
mm = int(input("Masukkan mm : " ))
ss = int(input("Masukkan ss : " ))

TotalDetik = (hh * 3600) + (mm * 60) + ss
print(TotalDetik)