import numpy as np
import random


data1 = np.array([])
print(data1)

data2 = np.array([5,7,3,9])
print(data2)

data3 = np.array([2.5,7.2,4.7])
print(data3)

data4 = np.array([2.5,7.25,5.2])
print(data4)

print(data2[3])

############################################
data = np.zeros(5)
for i in range(len(data)):
    data[i] = random.randint(10,100)
print('Data Awal : ',data)

# Traversal menampilkan data
for i in range(len(data)):
    print(i," berisi ",data[i])

# Traversal menghitung total
total = 0
for i in range(len(data)):
    total = total + data[i]
print("Total : ",total)

# Traversal mencari nilai terbesar
terbesar = data[0]
for i in range(len(data)):
    if data[i] > terbesar:
        terbesar = data[i]
print("Terbesar : ",terbesar)

# Traversal mencari nilai terkecil
terkecil = data[0]
for i in range(len(data)):
    if data[i] < terkecil:
        terkecil = data[i]
print("Terkecil : ",terkecil)