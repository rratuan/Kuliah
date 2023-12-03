#Program Konversi Detik
#I.S : Pengguna memasukkan total detik
#F.S : Program menampilkan hasil konversi ke hari, jam, menit,d detik

TotalDetik = int(input("masukkan Total Detik : "))

Hari = TotalDetik // (24*3600)
SisaHari = TotalDetik % (24*3600)

Jam = SisaHari // 3600
SisaJam = SisaHari % 3600

Menit = SisaJam // 60
Detik = SisaJam % 60

#Hasil Output
print ("Hasil Konversi ",TotalDetik,"Detik Adalah ",Hari," Hari, ",Jam," Jam, ",Menit," Menit, ",Detik," Detik")