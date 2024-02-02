import numpy as np
data = np.array([2,7,9,3,5,1])
# menampilkan seluruh elemen array
print('data :',data)
print('data[:] :',data[:])
# menampilkan elemen array dari index 1 sampai 2
print('data[1:3] :',data[1:3])
# menampilkan elemen array dari index awal sampai 4
print('data[:4] :',data[:4])
# menampilkan elemen array dari index awal sampai akhir tapi loncat 2 index
print('data[::2] :',data[::2])
# menjumlahkan semua elemen tapi loncat 2 index
print('sum :',sum(data[::2]))