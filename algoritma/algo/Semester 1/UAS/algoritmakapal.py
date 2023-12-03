# algoritmaperkapalan

# I.S. admin memasukkan jenis kapal yang akan berlabuh
# F.S. sistem menampilkan tanggal dan dek kapal tempat berlabuh

namakapal = []
tanggalmasuk = []
letak = []
jeniskapal = []


def masukkandata(namakapal, tanggalmasuk, letak, jeniskapal):
    nk = str(input("Masukkan Nama Kapal 	: ")).upper()
    jp = str(input("Jenis Kapal    (feri/kargo): ")).upper()
    namakapal.append(nk)
    jeniskapal.append(jp)
    if jp == "FERI":
        tm = int(input("Tanggal Masuk (yyyymmdd)	: "))
        ltk = "PELABUHAN1"
        tanggalmasuk.append(tm)
        letak.append(ltk)
    elif jp == "KARGO":
        tm = int(input("Tanggal Masuk (yyyymmdd)	: "))
        ltk = "PELABUHAN2"
        tanggalmasuk.append(tm)
        letak.append(ltk)


def TampilData(namakapal, tanggalmasuk, letak, jeniskapal):
    print('----Daftar Mahasiswa----')
    print('------------------------')
    for i in range(len(tanggalmasuk)):
        print('No  :', i+1, end='|')
        print('TanggalMasuk :', tanggalmasuk[i], end='|')
        print('NamaKapal :', namakapal[i], end='|')
        print('jeniskapal :', jeniskapal[i], end='|')
        print('letak :', letak[i], end='|')
        print()


def PengurutanData(namakapal, tanggalmasuk, letak, jeniskapal):
    n = len(tanggalmasuk)
    for i in range(n):
        for j in range(n-i-1):
            if tanggalmasuk[j] > tanggalmasuk[j+1]:

                temp = tanggalmasuk[j]
                tanggalmasuk[j] = tanggalmasuk[j+1]
                tanggalmasuk[j+1] = temp

                temp = letak[j]
                letak[j] = letak[j+1]
                letak[j+1] = temp

                temp = jeniskapal[j]
                jeniskapal[j] = jeniskapal[j+1]
                jeniskapal[j+1] = temp

                temp = namakapal[j]
                namakapal[j] = namakapal[j+1]
                namakapal[j+1] = temp


def CariNama(namakapal, tanggalmasuk, letak, jeniskapal):
    print("----------===5===----------")
    print("Cari Data Menurut : ")
    print("1. namakapal")
    print("2. tanggalmasuk")
    print("3. letak")
    print("4. jeniskapal")
    menu = int(input("Masukan Input Menu : "))
    ditemukan = []
    if menu == 1:
        Cari = str(input("Masukan Nama Kapal  : ")).upper()
        i = 0
        while i < len(namakapal):
            if Cari == namakapal[i]:
                ditemukan.append(i)
            i += 1
    elif menu == 2:
        Cari = int(input("Masukan Tanggal Masuk : "))
        i = 0
        while i < len(tanggalmasuk):
            if Cari == tanggalmasuk[i]:
                ditemukan.append(i)
            i += 1
    elif menu == 3:
        Cari = str(input("Masukan Letak : ")).upper()
        i = 0
        while i < len(letak):
            if Cari == letak[i]:
                ditemukan.append(i)
            i += 1
    elif menu == 4:
        Cari = str(input("Masukan Jenis Kapal : ")).upper()
        i = 0
        while i < len(jeniskapal):
            if Cari == jeniskapal[i]:
                ditemukan.append(i)
            i += 1
    else:
        print("Pilihan Tidak Ditemukan")
    for i in ditemukan:
        print('No  :', i+1, end='|')
        print('TanggalMasuk :', tanggalmasuk[i], end='|')
        print('NamaKapal :', namakapal[i], end='|')
        print('jeniskapal :', jeniskapal[i], end='|')
        print('letak :', letak[i], end='|')
        print()


def Menu():
    print("---==Menu==---")
    print("1. Memasukkan Data")
    print("2. Mengurutkan Data")
    print("3. Pencarian Data")
    print("0. Keluar")
    menu = int(input("Masukkan Pilihan : "))
    return menu


menu = Menu()
while (menu != 0):
    if(menu == 1):
        masukkandata(namakapal, tanggalmasuk, letak, jeniskapal)
    elif(menu == 2):
        PengurutanData(namakapal, tanggalmasuk, letak, jeniskapal)
        TampilData(namakapal, tanggalmasuk, letak, jeniskapal)
    elif(menu == 3):
        CariNama(namakapal, tanggalmasuk, letak, jeniskapal)
    menu = Menu()
