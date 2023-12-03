# Program Daftar_Nilai_Mahasiswa
# I.S.: 
# F.S.: 
MAKSBARIS = 99

import os


# Subrutin Mengisi
def IsiData(NIM, NamaMahasiswa, NilaiAkhir, N):
    print(f'<<< Mengisi Data Mahasiswa Sebanyak {N} >>>')
    print('=========================================')
    for i in range(N):
        print(f'<<< Data Mahasiswa Ke-{i+1} >>>')
        NIM[i] = int(input('NIM   : '))
        NamaMahasiswa[i] = input('Nama  : ')
        NilaiAkhir[i] = float(input('Nilai : '))
        print('-----------------------------------------')


# Subrutin Menampilkan
def TampilData(Kelas, MataKuliah, NIM, NamaMahasiswa, NilaiAkhir, N):
    print('                              Daftar Nilai Mahasiswa                              ')
    print(f'Kelas       : {Kelas}')
    print(f'Mata Kuliah : {MataKuliah}')
    print('==================================================================================')
    print(f'| No. |   NIM    |          Nama Mahasiswa          | Nilai Akhir | Indeks Nilai |')
    print('----------------------------------------------------------------------------------')
    for i in range(N):
        print(f'| {i+1:2}  | {NIM[i]:8} | {NamaMahasiswa[i]:32} | {NilaiAkhir[i]:11} |      {TentukanIndeksNilai(NilaiAkhir[i])}       |')
    print('==================================================================================')


# Subrutin Menu Nomor 1
def NIM_BubbleSortAscending(NIM, NamaMahasiswa, NilaiAkhir, N):
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if(NIM[j] < NIM[j - 1]):
                Temp = NIM[j]
                NIM[j] = NIM[j - 1]
                NIM[j - 1] = Temp
                Temp = NamaMahasiswa[j]
                NamaMahasiswa[j] = NamaMahasiswa[j - 1]
                NamaMahasiswa[j - 1] = Temp
                Temp = NilaiAkhir[j]
                NilaiAkhir[j] = NilaiAkhir[j - 1]
                NilaiAkhir[j - 1] = Temp

# Subrutin Menu Nomor 2
def NamaMahasiswa_BubbleSortDescending(NIM, NamaMahasiswa, NilaiAkhir, N):
    for i in range(N-1):
        for j in range(N-i-1):
            if(NamaMahasiswa[j] < NamaMahasiswa[j + 1]):
                Temp = NamaMahasiswa[j]
                NamaMahasiswa[j] = NamaMahasiswa[j + 1]
                NamaMahasiswa[j + 1] = Temp
                Temp = NIM[j]
                NIM[j] = NIM[j + 1]
                NIM[j + 1] = Temp
                Temp = NilaiAkhir[j]
                NilaiAkhir[j] = NilaiAkhir[j + 1]
                NilaiAkhir[j + 1] = Temp


# Subrutin Menu Nomor 3
def NilaiAkhir_MaximumSortAscending(NIM, NamaMahasiswa, NilaiAkhir, N):
    j = 0
    for i in range(N-1):
        max = 0
        for j in range(1, N-i):
            if (NilaiAkhir[j] > NilaiAkhir[max]):
                max = j
        NIM[j], NIM[max] = NIM[max], NIM[j]
        NamaMahasiswa[j], NamaMahasiswa[max] = NamaMahasiswa[max], NamaMahasiswa[j]
        NilaiAkhir[j], NilaiAkhir[max] = NilaiAkhir[max], NilaiAkhir[j]


# Subrutin Menentukan Indeks Nilai
def TentukanIndeksNilai(Nilai):
    if (Nilai <= 100) and (Nilai > 79):
        return 'A'
    elif (Nilai <= 80) and (Nilai > 69):
        return 'B'
    elif (Nilai <= 70) and (Nilai > 59):
        return 'C'
    elif (Nilai <= 60) and (Nilai > 49):
        return 'D'
    else:
        return 'E'


# Subrutin Menu Nomor 4
def IndeksNilai_MinimumSortDescending(NIM, NamaMahasiswa, NilaiAkhir, N):
    j = 0
    for i in range(N-1):
        min = 0
        for j in range(1, N-i):
            IndeksJ = TentukanIndeksNilai(NilaiAkhir[j])
            IndeksMin = TentukanIndeksNilai(NilaiAkhir[min])
            if (IndeksJ < IndeksMin):
                min = j
        NIM[j], NIM[min] = NIM[min], NIM[j]
        NamaMahasiswa[j], NamaMahasiswa[min] = NamaMahasiswa[min], NamaMahasiswa[j]
        NilaiAkhir[j], NilaiAkhir[min] = NilaiAkhir[min], NilaiAkhir[j]


# Subrutin Menu
def MenuPilihan(Kelas, MataKuliah, NIM, NamaMahasiswa, NilaiAkhir, N):
    os.system('pause')
    Pilihan = 1
    while (Pilihan != 0):
        os.system('cls')
        TampilData(Kelas, MataKuliah, NIM, NamaMahasiswa, NilaiAkhir, N)

        print('Pilihan Menu:')
        print('1. Urutkan Data Berdasarkan NIM (Ascending)')
        print('2. Urutkan Data Berdasarkan Nama Mahasiswa (Descending)')
        print('3. Urutkan Data Berdasarkan Nilai Akhir (Ascending)')
        print('4. Urutkan Data Berdasarkan Indeks Nilai (Descending)')
        print('0. Keluar')
        Pilihan = int(input('Pilihan Anda? '))

        while (Pilihan < 0) or (Pilihan > 4):
            print('Pilihan Salah. Ulangi!')
            Pilihan = int(input('Pilihan Anda? '))

        os.system('cls')

        if (Pilihan == 1):
            NIM_BubbleSortAscending(NIM, NamaMahasiswa, NilaiAkhir, N)
        elif (Pilihan == 2):
            NamaMahasiswa_BubbleSortDescending(NIM, NamaMahasiswa, NilaiAkhir, N)
        elif (Pilihan == 3):
            NilaiAkhir_MaximumSortAscending(NIM, NamaMahasiswa, NilaiAkhir, N)
        elif (Pilihan == 4):
            IndeksNilai_MinimumSortDescending(
                NIM, NamaMahasiswa, NilaiAkhir, N)


# Badan Algoritma Utama
# Penciptaan
NIM             = ['/'] * MAKSBARIS     # String
NamaMahasiswa   = ['/'] * MAKSBARIS     # String
NilaiAkhir      = [0.0] * MAKSBARIS     # Float

# Pengguna Memasukkan Jumlah Mahasiswa
os.system('cls')
Kelas       =     input('Kelas            : ')
MataKuliah  =     input('Mata Kuliah      : ')
N           = int(input('Jumlah Mahasiswa : '))
os.system('cls')

TampilData(Kelas, MataKuliah, NIM, NamaMahasiswa, NilaiAkhir, N)
os.system('pause')
os.system('cls')

IsiData(NIM, NamaMahasiswa, NilaiAkhir, N)

MenuPilihan(Kelas, MataKuliah, NIM, NamaMahasiswa, NilaiAkhir, N)
