import numpy as np

data = np.array([])
print("Data Awal : ",data)

# menambah data (variabel,value yang ditambahkan)
data = np.append(data,7)
data = np.append(data,10)
data = np.append(data,3)
data = np.append(data,5)
print("Data setelah penambahan : ",data)

# menyisipkan data (variabel,index posisi sisip,value sisip)
data = np.insert(data,2,9)
print("Data setelah insert 9 di posisi 3 : ",data)

# menghapus data (variabel.index dari value yg dihapus)
data = np.delete(data,1)
print("Data setelah hapus posisi 2 : ",data)
data = np.delete(data,0)
print("Data setelah hapus posisi 1 : ",data)

