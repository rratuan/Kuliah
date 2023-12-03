str_tgl = input('Tanggal [DD/MM/YYYY] : ').split('/')

# ketika user menginputkan misal 1/2/2023 maka akan di pisah setelah tanda '/'
# dan dimasukkan ke dalam str_tgl dengan 1 masuk ke index [0], 2 masuk ke index [1],dan 2023 masuk ke index [2]

tanggal = int(str_tgl[0])
bulan = int(str_tgl[1])
tahun = int(str_tgl[2])

if bulan in [1,3,5,7,8,10,12]:
    batasTanggal = 31
elif bulan in [4,6,9,11]:
    batasTanggal = 30
elif bulan == 2:
    if (tahun % 100 != 0)and(tahun % 4 == 0) or \
        (tahun % 100 == 0)and(tahun % 400 == 0):
        batasTanggal = 29
    else:
        batasTanggal = 28

if tanggal >= 1 and tanggal <= batasTanggal:
    print('Tanggal Valid')
else:
    print('Tanggal Tidak Valid')