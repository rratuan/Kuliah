#I.S memasukkan kedua tanggal yang akan di hitung jaraknya dengan format (dd,mm,yy)
#F.S menampilkan jarak antara kedua tanggal

#Input
dd1 = int(input("Masukan tanggal pertama dengan format (dd) : "))
mm1 = int(input("Masukan bulan pertama dengan format (mm) : "))
yy1 = int(input("Masukan tahun pertama dengan format (yy) : "))

dd2 = int(input("Masukan tanggal kedua dengan format (dd) : "))
mm2 = int(input("Masukan bulan kedua dengan format (mm) : "))
yy2 = int(input("Masukan tahun kedua dengan format (yy) : "))

#Cara Hitung

dd = dd2 - dd1
mm = (mm2 - mm1) *30
yy = (yy2 - yy1) *365

jarakhari = yy + mm + dd

#output
print("jarak hari : ",jarakhari)