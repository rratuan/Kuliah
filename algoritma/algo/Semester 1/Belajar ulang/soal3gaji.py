#I.S. Pengguna memasukkan nama karyawan, gaji pokok, tunjangan, pajak
#F.S. Sistem menampilkan gaji bersih

NamaKaryawan = str(input("Masukkan Nama Karyawan : " ))
GajiPokok = int(input("Masukkan Gaji Pokok : " ))
Tunjangan = int(input("Masukkan Tunjangan : " ))
Pajak = int(input("Masukkan Pajak : " ))

Tunjangan = 20/100 *GajiPokok
Pajak = 15/100 * GajiPokok
GajiBersih = (GajiPokok + Tunjangan - Pajak)

print(GajiBersih, "Total Gaji Bersih")