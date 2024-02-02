def kabisat(tahun):
    if ((tahun % 100 != 0) and (tahun % 4 == 0)) or ((tahun % 100 == 0) and (tahun % 400 == 0)):
        return True
    else:
        return False

def tanggalTerakhir(tahun, bulan):
    if bulan in [1,3,5,7,8,10,12]:
        return 31
    elif bulan in [4,6,9,11]:
        return 30
    elif bulan == 2:
        if kabisat(tahun):
            return 29
        else: 
            return 28

# testing
print('1998 :',kabisat(1998))
print('1996 :',kabisat(1996))
print('1900 :',kabisat(1900))
print('2000 :',kabisat(2000))

tahun = int(input('Inputkan Tahun : '))
if kabisat(tahun):
    print(tahun,'adalah tahun kabisat')
else:
    print(tahun,'bukanlah tahun kabisat')

print('1998-02 :', tanggalTerakhir(1998,2))
print('1998-01 :', tanggalTerakhir(1998,1))
print('2000-02 :', tanggalTerakhir(2000,2))

def hariKe(tahun,bulan,tanggal):
    hari = 0
    for thn in range(1900,tahun):
        if kabisat(thn):
            hari = hari + 366
        else:
            hari = hari + 365
    for bln in range(1,bulan):
        hari = hari + tanggalTerakhir(tahun,bln)
    hari = hari + tanggal
    return hari

# testing
print('1900-01-01 :',hariKe(1900,1,1))
print('1900-02-01 :',hariKe(1900,2,1))
print('1945-08-17 :',hariKe(1945,8,17))
print('2023-12-21 :',hariKe(2023,12,21))

hariLahir = hariKe(2005,6,13)
sekarang = hariKe(2023,12,21)

print('Umur Saya : ',(sekarang - hariLahir),'hari')
print('Biaya Hidup : ',(sekarang - hariLahir)*50000)