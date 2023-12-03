#Program array(:arik)
A = []
NMaks = 5

#Prosedure Untuk Menambah Array
def BacaLarik (A,n) :
    banyak_data = len(A)
    if(banyak_data<NMaks) and (n<=(NMaks-banyak_data)) :
        for i in range (n) : 
            data_baru = int(input('Masukkan Data Larik : '))
            A.append(data_baru)
    else :
        print('Maaf Data Penuh / Data Yang Bisa Dimasukan Sebanyak ',(NMaks-banyak_data))

def CetakLarik (A) :
    for Larik in A :
        print(Larik)

def Rata (A,banyak_data) :
    total = 0
    for Larik in A :
        total += Larik

    return total / banyak_data

def TertinggiTerendah (A) :
    NTertinggi = A[0]
    NTerendah = A[0]

    for Larik in A :
        if Larik < NTerendah :
            NTerendah = Larik
        elif Larik > NTertinggi :
            NTertinggi = Larik 
    
    print('Nilai Tertingi Adalah :',NTertinggi)
    print('Nilai Terendah Adalah :',NTerendah)

def SisipLarik(A,Posisi,Data) :
    banyak_data = len(A)
    if (banyak_data<NMaks) :
        A.insert(Posisi,Data)
    else :
        print('Maaf Data Penuh')

print('Menu')
print('1. Tulis Larik')
print('2. Lihat Element Larik')
print('3. Sisipkan Elemen')
print('4. Nilai Rata-Rata')
print('5. Nilai Tertinggi dan Terendah')
print('0. Keluar')
menu = int(input('Masukkan Pilihan : '))

while (menu!=0) :
    if (menu == 1):
        n = int(input('Masukkan Jumah Elemen Larik : '))
        BacaLarik(A,n)
    elif(menu == 2) :
        #CetakLarik(A)
        banyak_data = len(A)
        print(A)
        print(banyak_data)
    elif(menu == 3) :
        posisi = int(input('Masukkan Posisi Yang Diinginkan : '))
        data = int(input('Masukkan Data Larik : '))
        SisipLarik(A,posisi,data)
    elif(menu == 4) :
        banyak_data = len(A)
        print('Nilai Rata-Rata Dari',banyak_data,'Adalah :',Rata(A,banyak_data))
    elif(menu == 5) :
        TertinggiTerendah(A)

    print('-'*30)    
    menu = int(input('Masukkan Pilihan : '))