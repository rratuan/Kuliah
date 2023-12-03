#Program Menghitung Komisi Salesman
#S.S : Pengguna memasukkan nama salesman dan nilai penjualannya
#f.S : Program menampilkan nama salesman dan juga komisi yang diperoleh

#memasukkan nama salesman dan nilai penjualan
NamaSalesman = str(input("Masukkan Nama Salesman : "))
NilaiPenjualan = float(input("Masukkan Nilai Penjualan : "))

#menghitung Komisi
Komisi = 0.05 * NilaiPenjualan

#menampilkan nama salesman dan besaran komisi
print("Nama Salesman : ",NamaSalesman)
print("Besar Komisi : ",Komisi)