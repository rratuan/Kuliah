import random

def bubbleSort(data):
    N = len(data)
    for i in range(N):
        for j in range(N-1,i,-1):
            if data[j] < data[j-1]:
                data[j],data[j-1] = data[j-1],data[j]

def selectionSort(data):
    N = len(data)
    for i in range(N):
        idx_min = i
        for j in range(i+1,N):
            if data[j] < data[idx_min]:
                idx_min = j
        data[i],data[idx_min] = data[idx_min],data[i]

def getNamaBelakang(nama):
    nama_per_kata = nama.split(" ")
    return nama_per_kata[len(nama_per_kata) - 1] #diambil nama index terakhir

def removeArticle(judul):
    kata = str.upper(judul).split(" ")
    if kata[0] in ['A','AN','THE']:
        kata.pop(0)
    return ' '.join(kata)


data1 = [random.randint(1,100) for i in range(20)]
data2 = [random.randint(1,100) for i in range(20)]
data3 = ['Asep Supriatna','Budi Dharma','Cecep Permana','Dede Adi Agung']
data4 = ["An American Crime", "The Shawshank Redeption", "A Beautiful Mind", "Swallow", "The Crown", "American Beauty", "Pacific Rim"]

# bubble sort
print('Data Asli :',data1)
bubbleSort(data1)
print('Data terurut :',data1)
# selection sort
print('Data Asli :',data2)
selectionSort(data2)
print('Data terurut :',data2)
# mengurutkan berdasarkan nama belakang
print('Data Asli :',data3)
data3 = sorted(data3,key=getNamaBelakang)
print('Data terurut :',data3)
# mengurutkan dengan mengabaikan kata article tertentu
print('Data Asli :',data4)
data4 = sorted(data4,key=removeArticle)
print('Data terurut :',data4)