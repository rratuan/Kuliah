# Program Array atau Larik

# Prosedur Untuk Menambahkan Array
A = []


def BacaLarik(A, n):
    Banyakdata = len(A)
    if Banyakdata < 5:
        for i in range(n):
            databaru = int(input("Masukan data larik : "))
            A.append(databaru)
            Banyakdata = len(A)
    else:
        print("jumlah Data Tercapai")


def CetakLarik(A):
    for Larik in A:
        print(Larik)


def Menyisipkan(A, posisi, data):
    Banyakdata = len(A)
    if Banyakdata < 5:
        A.insert(posisi, data)
    else:
        print("Data Maximal Telah Dicapai")


print("menu")
print("1. Tulis Larik")
print("2. Lihat Element Larik")
print("3. Menyisipkan Larik")
print("0. Keluar")
Menu = int(input("Masukan Pilihan : "))

while Menu != 0:
    if (Menu == 1):
        Banyakdata = len(A)
        if (Banyakdata < 5):
            n = int(input("Masukan Jumlah element Larik : "))
            if n < 5:
                BacaLarik(A, n)
            else:
                print("Data Melebihi Nilai Maximum")
        else:
            print("Data Maximal Telah Dicapai")

    if (Menu == 2):
        # CetakLarik(A)
        Banyakdata = len(A)
        print(Banyakdata)
        print(A)
    if (Menu == 3):
        Banyakdata = len(A)
        if Banyakdata < 5:
            posisi = int(input("Masukan Posisi Insert : "))
            data = int(input("Masukan Jumah element Larik : "))
            Menyisipkan(A, posisi, data)
        else:
            print("Data Maximal Telah Dicapai")

    print("-"*30)
    Menu = int(input("Masukan Pilihan : "))