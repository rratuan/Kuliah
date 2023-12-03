tanggal = int(input("Masukkan Tanggal : "))
bulan   = int(input("Masukkan Bulan : "))
tahun   = int(input("Masukkan Tahun : "))
match tanggal:
    case tanggal if ((tanggal >= 1) and (tanggal <= 31)) and (bulan == 1 and 3 and 5 and 7 and 8 and 10 and 12) and (tahun >= 0):
        print("1")
    case tanggal if ((tanggal >= 1) and (tanggal <= 30)) and (bulan == 4 and 6 and 9 and 11) and (tahun >= 0):
        print("2")
    case tanggal if ((tanggal >= 1) and (tanggal <= 29)) and (bulan == 2) and ((tahun % 4 == 0) and (tahun % 100 != 0) or (tahun % 400 == 0)):
        print("3")
    case tanggal if ((tanggal >= 1) and (tanggal <= 28)) and (bulan == 2) and ((tahun % 4 != 0) and (tahun % 100 == 0) or (tahun % 400 != 0)):
        print("4")
    case _:
        print("5")


[Tahun Kabisat]
1936, 1964, 1992, 2020, atau 2048

[Note]
"3" Kabisat
"4" Tidak