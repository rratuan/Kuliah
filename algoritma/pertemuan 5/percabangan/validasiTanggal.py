print(' Validasi Tanggal '.center(30,'='))

# input tanggal,bulan,tahun
tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan   : '))
tahun = int(input('Tahun   : '))

#deklarasi nilai awal bertujuan untuk memperluas scope agar tidak menimbulkan error di percabangan 
validasi = False #nilai awal validasi 

# validasi bulan
if 1 <= bulan <= 12 :
    # validasi tanggal
    if (bulan in [1,3,5,7,8,10,12] and 1 <= tanggal <= 31):
        validasi = True
    elif (bulan in [4,6,9,11] and 1 <= tanggal <= 30):
        validasi = True
    elif bulan == 2:
        if 1 <= tanggal <= 28:
            validasi = True
        elif 1 <= tanggal <= 29:
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 100 == 0 and tahun % 400 == 0):
                validasi = True

if validasi:
    x = 'Tanggal Valid'
else:
    x = 'Tanggal tidak Valid'

print(f'Tanggal {tanggal}/{bulan}/{tahun} adalah {x}')