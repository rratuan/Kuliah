import numpy as np

def sequentialSearch(data,dicari):
    posisi = 0
    while data[posisi] != dicari and posisi < len(data) - 1:
        posisi = posisi + 1
        if data[posisi] == dicari:
            return posisi
        else:
            return -1
    
def binarySearch(data, dicari):
    L = 0
    R = len(data) - 1
    C = (L + R) // 2
    while data[C] != dicari and L <= R:
        if data[C] < dicari:
            L = C + 1
        elif data[C] > dicari:
            R = C - 1
        C = (L + R) // 2
    if data[C] == dicari:
        return C
    else:
        return -1

def findsubstr(data, dicari):
    posisi = 0
    while data[posisi] != dicari and posisi < len(data)-1:
        posisi = posisi + 1
    if data[posisi] == dicari:
        return posisi
    else:
        return -1
    
def findallsubstr(data, dicari):
    hasil = []
    for index,elemen in enumerate(data):
        if str.upper(dicari) in str.upper(elemen):
            hasil.append(elemen)
    return hasil

#tester
# sequencial search
# data = np.random.randint(1,100,20) #random 1...100 sebanyak 20
# print('data:',data)
# dicari = int(input('Data yang dicari : '))
# posisi = sequentialSearch(data,dicari)
# if posisi >= 0:
#     print('Data ditemukan di posisi',posisi)
# else:
#     print('Data tidak ditemukan')

# binary search
# data = np.random.randint(1,100,20) #random 1...100 sebanyak 20
# data = sorted(data) #urutkan datanya terlebih dahulu
# print('data:',data)
# dicari = int(input('Data yang dicari : '))
# posisi = binarySearch(data,dicari)
# if posisi >= 0:
#     print('Data ditemukan di posisi',posisi)
# else:
#     print('Data tidak ditemukan')

# searching menggunakan 'in' tanpa mengetahui posisi
# data = np.random.randint(1,100,20) #random 1...100 sebanyak 20
# print('data:',data)
# dicari = int(input('Data yang dicari : '))
# if dicari in data:
#     print('Data ditemukan')
# else:
#     print('Data tidak ditemukan')

# searching menggunakan index()
# data = [6,9,2,5,3,7,1,0]
# print('data:',data)
# dicari = int(input('Data yang dicari : '))
# posisi = data.index(dicari)
# if posisi >= 0:
#     print('Data ditemukan di posisi',posisi)
# else:
#     print('Data tidak ditemukan')

# menelusuri angka yang di cari dalam sebuah array
# data = np.random.randint(1,10,20) #random 1...10 sebanyak 20
# print('data:',data)
# dicari = int(input('Data yang dicari : '))
# hasil = data >= dicari
# for index,isi in enumerate(hasil):
#     if isi == True:
#         print('Data ditemukan di posisi',index)

# menelusuri angka yang di cari dengan numpy where()
# data = np.random.randint(1,10,20) #random 1...10 sebanyak 20
# print('data:',data)
# dicari = int(input('Data yang dicari : '))
# hasil = np.where(data == dicari)
# for index,isi in np.ndenumerate(hasil):
#     print('Data ditemukan di posisi',isi)
    
# searching tipe data string menggunakan findsubstr function
# siswa = ['asep','dede','febri','jajang','unyil']
# dicari = input('Nama  Siswa : ')
# posisi = findsubstr(siswa,dicari)
# if posisi >= 0:
#     print('Data ditemukan di posisi',posisi)
# else:
#     print('Data tidak ditemukan')

# searching tipe data string meskii satu huruf menggunakan findallsubstr function
siswa = ['asep','dede','febri','jajang','unyil']
dicari = input('Nama  Siswa : ')
posisi = findallsubstr(siswa,dicari)
print('posisi data',posisi)

