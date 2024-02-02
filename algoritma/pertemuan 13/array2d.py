import numpy as np
import random as rnd

matrik = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12]
        ]

matrik2 = np.array([
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12]
        ])

# matriks yang valuenya 0 dengan baris 4 kolom 3
matrik3 = np.zeros((4,3))

# matriks yang valuenya 1 dengan baris 4 kolom 3
matrik4 = np.ones((4,3))

# matriks yang valuenya full 100 dengan baris 4 kolom 3
matrik5 = np.full((4,3),100)

# matriks yang valuenya kosong dengan baris 4 kolom 3
matrik6 = np.empty((4,3))

# matriks yang valuenya random dari 0-100 dengan baris 5 kolom 5
matrik7 = np.zeros((5,5))
for baris in range(len(matrik7)):
    for kolom in range(len(matrik7[baris])):
        matrik7[baris][kolom] = rnd.randint(0,100)

# matriks untuk gambar
matrik8 = np.zeros((10,30))
for baris in range(len(matrik8)):
    for kolom in range(len(matrik8[baris])):
        matrik8[baris][kolom] = rnd.randint(0,1)

print('Matriks : ',matrik)
print('Baris 1 : ',matrik[0])
print('Baris 2 : ',matrik[1])
print('Baris 3 : ',matrik[2])
print('Baris 4 : ',matrik[3])
print('Baris 1 Kolom 3 : ',matrik[0][2])
print('Baris 4 Kolom 2 : ',matrik[3][1])
print('Matriks 2 : ',matrik2)
print('Matriks 3 : ',matrik3)
print('Matriks 4 : ',matrik4)
print('Matriks 5 : ',matrik5)
print('Matriks 6 : ',matrik6)
print('Matriks 7 : ',matrik7)

print('Gambar : ')
for baris in range(len(matrik8)):
    for kolom in range(len(matrik8[baris])):
        if(matrik8[baris][kolom] == 0):
            print('x',end='')
        else:
            print(' ',end='')
    print() #setiap akhir baris,pindah baris