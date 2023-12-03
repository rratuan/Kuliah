# Program DaftarGajiPegawai
# I.S. : pengguna memasukkan Bulan, Tahun, Banyak Data Pegawai, NIP, Nama, Gol
# F.S. : menampilkan daftar gaji pegawai

import os

MAKS_PEGAWAI = 20  # Konstanta pegawai

# Subrutin PilihBulan
def PilihBulan():
    Bulan = int(input('Bulan (01 - 12) : '))

    while (Bulan < 1 or Bulan > 12):
        print('Bulan harus diantara 01-12, ulangi!')
        Bulan = int(input('Bulan (01 - 12) : '))

    return Bulan


# Subrutin HitungGajiPokok
def HitungGajiPokok(Gol):
    if (Gol == 'I'):
        return 1250000
    elif (Gol == 'II'):
        return 1350000
    elif (Gol == 'III'):
        return 1500000
    elif (Gol == 'IV'):
        return 1750000
    else:
        return 0


# Subrutin HitungTunjangan
def HitungTunjangan(Gol):
    if (Gol == 'I'):
        return 1250000 * 0.1
    elif (Gol == 'II'):
        return 1350000 * 0.125
    elif (Gol == 'III'):
        return 1500000 * 0.15
    elif (Gol == 'IV'):
        return 1750000 * 0.2
    else:
        return 0


# Subrutin TampilPegawai
def TampilPegawai(Bulan, Tahun, NIP, Nama, Gol, N):
    print('                                                   DAFTAR GAJI PEGAWAI')
    print(f'Bulan/Tahun : {Bulan}/{Tahun}')

    print(
        '---------------------------------------------------------------------------------------------------------------------')
    print(
        '| No |    NIP    |     Nama Pegawai     | Gol. |   Gaji Pokok   |   Tunjangan   |       PPN      |    Gaji Total    |')
    print(
        '---------------------------------------------------------------------------------------------------------------------')

    for i in range(N):
        GajiPokok = HitungGajiPokok(Gol[i])
        Tunjangan = HitungTunjangan(Gol[i])

        GajiTotal = GajiPokok + Tunjangan
        PPN = 0.1 * GajiTotal
        GajiTotal = GajiTotal - PPN

        print(
            f'| {i + 1:2} | {NIP[i]:9} | {Nama[i]:20} | {Gol[i]:4} | Rp. {GajiPokok:>10} | Rp. {Tunjangan:>9.1f} | Rp. {PPN:>10.1f} | Rp. {GajiTotal:>12.1f} |')

    print(
        '---------------------------------------------------------------------------------------------------------------------')


# Subrutin IsiPegawai
def IsiPegawai(NIP, Nama, Gol, N):
    print(f'<<< Memasukkan Data Pegawai Sebanyak {N} Pegawai >>>')
    print()

    for i in range(N):
        print(f'Data Pegawai Ke-{i + 1}')
        print('-------------------------')

        NIP[i] = str(input('Nomor Induk Pegawai (NIP) : '))
        Nama[i] = str(input('Nama Pegawai              : '))
        Gol[i] = str(input('Golongan (I,II,III,IV)    : '))

        # Validasi golongan
        while (Gol[i] != 'I' and Gol[i] != 'II' and Gol[i] != 'III' and Gol[i] != 'IV'):
            print('Golongan harus antara I-IV, ulangi!')
            Gol[i] = str(input('Golongan (I,II,III,IV)    : '))

        print()


# Subrutin menu pilihan
def MenuPilihan():
    print('MENU PENGURUTAN')
    print('---------------')
    print('1. NIP')
    print('2. Golongan')
    print('3. Tunjangan')
    print('4. Gaji Total')
    print('0. Keluar')

    Menu = int(input('Pilihan Anda : '))

    while (Menu < 0 or Menu > 4):
        print('Pilihan harus diantara 0-4, ulangi!')
        Menu = int(input('Pilihan Anda? '))

    return Menu


# Subrutin Pengurutan Bubble Sort Ascending
def BubbleSortAsc(NIP, Nama, Gol, N):  # For Downto Do
    for i in range(N - 1):
        for j in range(N - 1, i, -1):
            if (NIP[j] < NIP[j - 1]):
                NIP[j], NIP[j - 1] = NIP[j - 1], NIP[j]
                Nama[j], Nama[j - 1] = Nama[j - 1], Nama[j]
                Gol[j], Gol[j - 1] = Gol[j - 1], Gol[j]


# Subrutin Pengurutan Bubble Sort Descending
def BubbleSortDsc(NIP, Nama, Gol, N):  # For To Do
    for i in range(N - 1):
        for j in range(N - i):
            if (Gol[j] < Gol[j + 1]):
                NIP[j], NIP[j + 1] = NIP[j + 1], NIP[j]
                Nama[j], Nama[j + 1] = Nama[j + 1], Nama[j]
                Gol[j], Gol[j + 1] = Gol[j + 1], Gol[j]


# Subrutin Pengurutan Minimum Sort Ascending
def MinSortAsc(NIP, Nama, Gol, N):
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            Tunjangan = HitungTunjangan(Gol[j])
            TunjanganMin = HitungTunjangan(Gol[min])

            if (Tunjangan < TunjanganMin):
                min = j

        NIP[i], NIP[min] = NIP[min], NIP[i]
        Nama[i], Nama[min] = Nama[min], Nama[i]
        Gol[i], Gol[min] = Gol[min], Gol[i]


# Subrutin Pengurutan Maximum Sort Descending
def MaxSortDsc(NIP, Nama, Gol, N):
    for i in range(N - 1):
        max = i  # Asumsi Nilai Maksimum Di Indeks i (Pertama)
        for j in range(i + 1, N):
            GajiPokok = HitungGajiPokok(Gol[j])
            Tunjangan = HitungTunjangan(Gol[j])

            GajiTotal = GajiPokok + Tunjangan
            PPN = 0.1 * GajiTotal
            GajiTotal = GajiTotal - PPN

            GajiPokok2 = HitungGajiPokok(Gol[max])
            Tunjangan2 = HitungTunjangan(Gol[max])

            GajiTotal2 = GajiPokok2 + Tunjangan2
            PPN2 = 0.1 * GajiTotal2
            GajiTotal2 = GajiTotal2 - PPN2

            if (GajiTotal > GajiTotal2):
                max = j

        NIP[i], NIP[max] = NIP[max], NIP[i]
        Nama[i], Nama[max] = Nama[max], Nama[i]
        Gol[i], Gol[max] = Gol[max], Gol[i]


# Program utama
Bulan = PilihBulan()
Tahun = int(input('Tahun           : '))
os.system('pause')
os.system('cls')

NIP = ['/'] * MAKS_PEGAWAI
NIP2 = ['/'] * MAKS_PEGAWAI
Nama = ['/'] * MAKS_PEGAWAI
Nama2 = ['/'] * MAKS_PEGAWAI
Gol = ['/'] * MAKS_PEGAWAI
Gol2 = ['/'] * MAKS_PEGAWAI

# Penciptaan
print('<<< Hasil Proses Penciptaan >>>')
print()
TampilPegawai(Bulan, Tahun, NIP, Nama, Gol, MAKS_PEGAWAI)
os.system('pause')
os.system('cls')

# Banyak Data Pegawai
N = int(input('Banyak Data Pegawai : '))

while (N < 0 or N > MAKS_PEGAWAI):
    print('Banyak Data Pegawai tidak boleh kurang dari 0 dan lebih dari', MAKS_PEGAWAI)
    N = int(input('Banyak Data Pegawai : '))
os.system('pause')
os.system('cls')

# Isi Pegawai
IsiPegawai(NIP, Nama, Gol, N)
os.system('pause')
os.system('cls')

# Tampil Data Pegawai
TampilPegawai(Bulan, Tahun, NIP, Nama, Gol, N)
os.system('pause')
os.system('cls')

# Menu Pilihan
Menu = MenuPilihan()
os.system('pause')
os.system('cls')
while (Menu != 0):
    if (Menu == 1):
        # Bubble Sort Asc
        print('<<< NIP Terurut Ascending (Bubble Sort) >>>')
        print()
        NIP2 = NIP
        Nama2 = Nama
        Gol2 = Gol
        BubbleSortAsc(NIP2, Nama2, Gol2, N)
        TampilPegawai(Bulan, Tahun, NIP2, Nama2, Gol2, N)
        os.system('pause')
        os.system('cls')
    elif (Menu == 2):
        # Bubble Sort Dsc
        print('<<< Golongan Pegawai Terurut Descending (Bubble Sort) >>>')
        print()
        NIP2 = NIP
        Nama2 = Nama
        Gol2 = Gol
        BubbleSortDsc(NIP2, Nama2, Gol2, N)
        TampilPegawai(Bulan, Tahun, NIP2, Nama2, Gol2, N)
        os.system('pause')
        os.system('cls')
    elif (Menu == 3):
        # Minimum Sort Asc
        print('<<< Tunjangan Pegawai Terurut Ascending (Minimum Sort) >>>')
        print()
        NIP2 = NIP
        Nama2 = Nama
        Gol2 = Gol
        MinSortAsc(NIP2, Nama2, Gol2, N)
        TampilPegawai(Bulan, Tahun, NIP2, Nama2, Gol2, N)
        os.system('pause')
        os.system('cls')
    else:
        # Maximum Sort Dsc
        print('<<< Gaji Total Pegawai Terurut Descending (Maximum Sort) >>>')
        print()
        NIP2 = NIP
        Nama2 = Nama
        Gol2 = Gol
        MaxSortDsc(NIP2, Nama2, Gol2, N)
        TampilPegawai(Bulan, Tahun, NIP2, Nama2, Gol2, N)
        os.system('pause')
        os.system('cls')

    print()
    Menu = MenuPilihan()
    os.system('pause')
    os.system('cls')