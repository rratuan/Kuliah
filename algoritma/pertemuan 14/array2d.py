import numpy as np

mat1 = np.array([ [2,7,8],[2,6,4] ])
for barisdata in mat1:
    for elemen in barisdata:
        print(elemen, end=" ")
    print()

print('Ukuran :',mat1.shape)

ukuran = mat1.shape
maxbaris = ukuran[0]
maxkolom =ukuran[1]
for baris in range(maxbaris):
    for kolom in range(maxkolom):
        print(mat1[baris,kolom],end=" ")
    print()

for index,elemen in np.ndenumerate(mat1):
    print(index,"==>",elemen)