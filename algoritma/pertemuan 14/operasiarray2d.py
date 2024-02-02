import numpy as np

def penjumlahan(m1,m2):
    m3 = np.zeros(m1.shape)
    for baris in range(m3.shape[0]):
        for kolom in range(m3.shape[1]):
            m3[baris,kolom] = m1[baris,kolom] + m2[baris,kolom]
    return m3

def pengurangan(m1,m2):
    m3 = np.zeros(m1.shape)
    for baris in range(m3.shape[0]):
        for kolom in range(m3.shape[1]):
            m3[baris,kolom] = m1[baris,kolom] - m2[baris,kolom]
    return m3

def perkalian(m1,m2):
    m5 = np.zeros((m1.shape[0],m2.shape[1]))
    for baris in range(m5.shape[0]):
        for kolom in range(m5.shape[1]):
            m5[baris,kolom] = 0
            for i in range(m1.shape[1]):
                m5[baris,kolom] = m5[baris,kolom] + m1[baris,i] * m2[i,kolom]
        return m5

def view(m):
    for baris in range(m.shape[0]):
        for kolom in range(m.shape[1]):
            print(m[baris,kolom], end=" ")
        print()

# tester
mat1 = np.array([ [1,2,3],[4,5,6],[7,8,9] ])
mat2 = np.array([ [1,2,3],[4,5,6],[7,8,9] ])
mat3 = penjumlahan(mat1,mat2)
mat4 = pengurangan(mat1,mat2)
mat5 = perkalian(mat1,mat2)
view(mat3)
view(mat4)

print('Matriks 1 :')
view(mat1)
print('Matriks 2 :')
view(mat2)
print('Matriks 3 :')
view(mat3)
print('Matriks 4 :')
view(mat4)
print('Matriks 5:')
view(mat5)