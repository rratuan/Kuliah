#Program Menghitung Waktu Pelari
#I.S : Pengguna memasukkan jam, menit, dan detik dari pelari
#F.S : Program menampilkan hasil konversi ke detik

#Memaskkan Nilai Jam Menit Detik
Jam = int(input("Masukkan Nilai Jam : "))
Menit = int(input("Masukkan Nilai Menit : "))
Detik  = int(input("Masukkan Nilai Detik : "))

#Menghitung Total Detik
TotalDetik = int((jam*3600) + (Menit*360) + Detik)

#Menampilkan Total Detik
print(TotalDetik)