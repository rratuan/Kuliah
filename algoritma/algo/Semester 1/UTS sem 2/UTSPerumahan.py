from operator import truediv


class Node:
    def __init__(self, pemilik, kluster, nama_jalan, blok, nomor_rumah):

        self.pemilik = pemilik
        self.kluster = kluster
        self.nama_jalan = nama_jalan
        self.blok = blok
        self.nomor_rumah = nomor_rumah
        self.next = None


class Perumahan:
    def __init__(self):
        self.awal = None

    def isEmpty(self):
        return self.awal is None

    def TampilData(self):
        # print('Isi Linked List : ', end='')
        if self.isEmpty():
            print('Data Kosong')
            input("Tekan Enter Untuk Kembali Ke Menu")
        else:
            print("Menampilkan Data")
            bantu = self.awal
            while bantu is not None:
                print(bantu.pemilik, bantu.kluster, bantu.nama_jalan,
                      bantu.blok, bantu.nomor_rumah, end="")
                if (bantu.next is not None):
                    print("->", end="")
                bantu = bantu.next
            print()

    def Penghancuran(self):
        Phapus = self.awal
        while (Phapus is not None):
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

    def pencarian(self):
        if self.isEmpty():
            print("Data Kosong")
        else:
            Caripemilik = str(input("Masukkan Nama Pemilik : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.pemilik == Caripemilik):
                    ketemu = True
                else:
                    bantu = bantu.next

            if (ketemu):
                print("pemilik", Caripemilik, "Ditemukan")
                print("Isi Perumahan : ")
                if self.isEmpty():
                    print("Data Kosong")
                else:
                    while (bantu is not None) and (Caripemilik == bantu.pemilik):
                        print(bantu.pemilik, bantu.kluster,
                              bantu.nama_jalan, bantu.blok, bantu.nomor_rumah)
                        bantu = bantu.next
                    print()
            else:
                print("pemilik", Caripemilik, "Tidak Ditemukan")

    def ubahdata(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            ubahpemilik = str(input("Masukkan Nama Yang Ingin Diubah : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if(bantu.pemilik == ubahpemilik):
                    ketemu = True
                else:
                    bantu = bantu.next
                if(ketemu):
                    pemilik = str(input("Nama Pemilik : "))
                    kluster = str(input("Nama Kluster : "))
                    nama_jalan = str(input("Nama Jalan : "))
                    blok = str(input("Blok : "))
                    nomor_rumah = int(input("Nomor Rumah : "))
                    bantu.pemilik = pemilik
                    bantu.kluster = kluster
                    bantu.nama_jalan = nama_jalan
                    bantu.blok = blok
                    bantu.nomor_rumah = nomor_rumah
                else:
                    print("Data", ubahpemilik,
                          "Yang akan diubah tidak ditemukan")

    def SisipDepan(self, pemilik, kluster, nama_jalan, blok, nomor_rumah):
        Baru = Node(pemilik, kluster, nama_jalan, blok, nomor_rumah)
        if (self.isEmpty()):
            self.awal = Baru
        else:
            Baru.next = self.awal
        self.awal = Baru

    def SisipBelakang(self, pemilik, kluster, nama_jalan, blok, nomor_rumah):
        Baru = Node(pemilik, kluster, nama_jalan, blok, nomor_rumah)
        if (self.isEmpty()):
            self.awal = Baru
        else:
            bantu = self.awal
            while (bantu.next is not None):
                bantu = bantu.next
            bantu.next = Baru

    def Hapus(self):
        bantu = self.awal
        if (bantu.next is None):
            return True
        else:
            return False

    def HapusDepan(self):
        Phapus = self.awal
        Elemen = Phapus.pemilik
        if (self.Hapus()):
            self.awal = None
        else:
            self.awal = Phapus.next

        del Phapus

    def HapusBelakang(self):
        if(self.Hapus()):
            Phapus = self.awal
            self.awal = None
        else:
            Phapus = self.awal
            while (Phapus.next is not None):
                Phapus = Phapus.next
            bantu = self.awal
            while (bantu.next is not Phapus):
                bantu = bantu.next

            bantu.next = None

        Elemen = Phapus.pemilik
        del Phapus

    def HapusTengah(self):
        if(self.isEmpty()):
            print("")
        else:
            HapusData = str(input("Masukkan Pemilik : "))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None):
                if (Phapus.pemilik == HapusData):
                    ketemu = True
                else:
                    Phapus = Phapus.next
            if(ketemu):
                Elemen = Phapus.pemilik
                if(Phapus.next == None):
                    self.HapusBelakang()
                elif(Phapus == self.awal):
                    self.HapusDepan()
                else:
                    bantu = self.awal
                    while(bantu.next is not Phapus):
                        bantu = bantu.next

                    bantu.next = Phapus.next
                    del Phapus

    def UrutDataAsc(self):
        if(self.isEmpty()):
            print("Data Tidak Ditemukan")
        else:
            i = self.awal
            while (i.next is not None):
                min = i
                j = i.next
                while (j is not None):
                    if(j.nomor_rumah < min.nomor_rumah):
                        min = j
                    j = j.next

            # Proses pertukaran dua Buah Data
            temp = min.pemilik, min.kluster, min.nama_jalan, min.blok, min.nomor_rumah
            min.pemilik, min.kluster, min.nama_jalan, min.blok, min.nomor_rumah = i.pemilik, i.kluster, i.nama_jalan, i.blok, i.nomor_rumah
            i.pemilik, i.kluster, i.nama_jalan, i.blok, i.nomor_rumah = temp

            # Menempatkan pointer i ke simpul berikutnya
            i = i.next


def Menu():
    print("=============================================")
    print("Menu Aplikasi Data Perumahan LinkedList python |")
    print("===============================================|")
    print("| 1. Input Data                                |")
    print("| 2. Tampilkan Data                            |")
    print("| 3. Hapus Data                                |")
    print("| 4. Ubah Data                                 |")
    print("| 5. Pencarian Data                            |")
    print("| 6. Urutkan Data                              |")
    print("| 0. Keluar Aplikasi                           |")
    print("===============================================|")
    menu = int(input("Masukkan pilihan anda : "))
    return menu


list1 = Perumahan()
menu = Menu()
while menu != 0:
    if menu == 1:
        # print('input data')
        pemilik = str(input("Nama Pemilik : "))
        kluster = str(input("Nama Kluster : "))
        nama_jalan = str(input("Nama Jalan : "))
        blok = str(input("Blok : "))
        nomor_rumah = int(input("Nomor Rumah : "))
        if (list1.isEmpty()):
            list1.SisipDepan(pemilik, kluster, nama_jalan, blok, nomor_rumah)
        else:
            list1.SisipBelakang(
                pemilik, kluster, nama_jalan, blok, nomor_rumah)
    elif menu == 2:
        list1.TampilData()
    elif menu == 3:
        list1.HapusTengah()
    elif menu == 4:
        list1.ubahdata()
    elif menu == 5:
        list1.pencarian()
    elif menu == 6:
        list1.UrutDataAsc()
    elif menu == 0:
        print('Keluar Aplikasi')
    else:
        print('Pilihan menu tidak ada!')
    menu = Menu()
else:
    print('Thanks')
    list1.Penghancuran()
