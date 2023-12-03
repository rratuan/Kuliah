class Node:
    def __init__(self, pemilik, kluster, nama_jalan, blok, nomor_rumah) :
        
        self.pemilik = pemilik
        self.kluster = kluster
        self.nama_jalan = nama_jalan
        self.blok = blok
        self.nomor_rumah = nomor_rumah
        self.next = None
class Perumahan:
    def __init__(self):
        self.awal = None        
    def isEmpty(self) :
        return self.awal is None

    def TampilData(self):
        # print('Isi Linked List : ', end='')
        if self.isEmptypemilik():
            print('Data Kosong')
            input("Tekan Enter Untuk Kembali Ke Menu")
        else:
            pemilik = self.pemilik
            kluster = self.kluster
            nama_jalan = self.nama_jalan
            blok = self.blok
            nomor_rumah = self.nomor_rumah
            while(pemilik is not None) and (kluster is not None) and (nama_jalan is not None) and (blok is not None) and (nomor_rumah is not None):
                print('=================================')
                print('| Pemilik Rumah           :',pemilik.info)
                print('| Kluster                 :',kluster.info)
                print('| Nama Jalan              :',nama_jalan.info)
                print('| Blok                    :',blok.info)
                print('| Nomor Rumah              :',nomor_rumah.info)
                print('=================================')
                pemilik = pemilik.next
                kluster = kluster.next
                nama_jalan = nama_jalan.next
                blok = blok.next
                nomor_rumah = nomor_rumah.next
            input("Tekan Enter Untuk Kembali Ke Menu")
            print()

    def PenghancuranPemilik(self):
        Phapus = self.awal
        while (Phapus is not None):
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

    def inputPemilik(self,DataPemilik):
        Pemilik = Node(DataPemilik)
        if(self.isEmptypemilik()):
            self.pemilik= Pemilik
        else:
            Pemilik.next = self.pemilik
            self.pemilik.prev = Pemilik
        self.pemilik = Pemilik
        
    def inputKluster(self,DataKluster):
        Kluster = Node(DataKluster)
        if(self.isEmptykluster()):
            self.kluster= Kluster
        else:
            Kluster.next = self.kluster
            self.kluster.prev = Kluster
        self.kluster = Kluster
        
    def inputnamajalan(self,Datanamajalan):
        namajalan = Node(Datanamajalan)
        if(self.isEmptynamajalan()):
            self.nama_jalan= namajalan
        else:
            namajalan.next = self.nama_jalan
            self.nama_jalan.prev = namajalan
        self.nama_jalan = namajalan

    def inputblok(self,Datablok):
        Blok = Node(Datablok)
        if(self.isEmptyblok()):
            self.blok = Blok
        else:
            Blok.next = self.blok
            self.blok.prev = Blok
        self.blok = Blok
    
    def inputnomorrumah(self,Datanomorrumah):
        NomorRumah = Node(Datanomorrumah)
        if(self.isEmptynomorrumah()):
            self.nomor_rumah = NomorRumah
        else:
            NomorRumah.next = self.nomor_rumah
            self.nomor_rumah.prev = NomorRumah
        self.nomor_rumah = NomorRumah

    # Penghapusan Belakang
    # def HapusBelakangDouble(self):
    #     if(self.isEmpty()):
    #         print('Data Kosong')
    #     else:
    #         Phapus = self.akhir
    #         Elemen = Phapus.info
    #         if(self.isEmpty()):
    #             self.awal = None
    #             self.akhir = None
    #         else:
    #             self.akhir = Phapus.prev
    #             self.akhir.next = None

    #         del Phapus
    #         print('Data Yang Dihapus Adalah : ', Elemen)
    
    def SatuNode(self) :
        HapusPemilik = self.pemilik
        if (HapusPemilik.next is None) :
            return True
        else :
            return False

    def hapusdatabelakang(self):
        if(self.isEmptypemilik() and self.isEmptykluster() and self.isEmptynamajalan() and self.isEmptyblok() and self.isEmptynomorrumah()) :
            print('Data Kosong')
        else :
            HapusPemilik = self.pemilik
            HapusKluster = self.kluster
            HapusNamaJalan = self.nama_jalan
            HapusBlok = self.blok
            HapusNomorRumah = self.nomor_rumah
            if(self.SatuNode()) :
                self.pemilik = None
                self.kluster = None
                self.nama_jalan = None
                self.blok = None
                self.nomor_rumah = None
            else :
                #Penacarian Node Terakhir
                while (HapusPemilik.next is not None):
                    HapusPemilik = HapusPemilik.next
                    HapusKluster = HapusKluster.next
                    HapusNamaJalan = HapusNamaJalan.next
                    HapusBlok = HapusBlok.next
                    HapusNomorRumah = HapusNomorRumah.next

                #Pencarian Node Sebelum Node Terakhir
                bantu = self.pemilik
                bantu1 = self.kluster
                bantu2 = self.nama_jalan
                bantu3 = self.blok
                bantu4 = self.nomor_rumah
                while (bantu.next is not HapusPemilik):
                    bantu = bantu.next
                    bantu1 = bantu1.next
                    bantu2 = bantu2.next
                    bantu3 = bantu3.next
                    bantu4 = bantu4.next

                bantu.next = None
                bantu1.next = None
                bantu2.next = None
                bantu3.next = None
                bantu4.next = None
            del HapusPemilik
            del HapusKluster
            del HapusNamaJalan
            del HapusBlok
            del HapusNomorRumah

    def hapusData(self):
        if(self.isEmptypemilik) and (self.isEmptykluster) and (self.isEmptynamajalan) and (self.isEmptyblok) and (self.isEmptynomorrumah):
            Pemilik = input('Masukan Nama Pemilik Rumah Yang Akan Dihapus : ')
            HapusPemilik = self.pemilik
            HapusKluster = self.kluster
            HapusNamaJalan = self.nama_jalan
            HapusBlok = self.blok
            HapusNomorRumah = self.nomor_rumah
            ketemu = False
            while (not ketemu) and (HapusPemilik is not None):
                if(HapusPemilik.info == Pemilik):
                    ketemu = True
                else:
                    HapusPemilik = HapusPemilik.next
                    HapusKluster = HapusKluster.next
                    HapusNamaJalan = HapusNamaJalan.next
                    HapusBlok = HapusBlok.next
                    HapusNomorRumah = HapusNomorRumah.next
            # print(HapusPemilik.info)
            
            if(ketemu):
                if(HapusPemilik == self.pemilik):
                    HapusPemilik = self.pemilik
                    if (self.SatuNode()) :
                         self.pemilik = None
                         self.kluster = None
                         self.nama_jalan = None
                         self.blok = None
                         self.nomor_rumah = None
                    else :
                        self.pemilik = HapusPemilik.next
                        self.kluster = HapusKluster.next
                        self.nama_jalan = HapusNamaJalan.next
                        self.blok = HapusBlok.next
                        self.nomor_rumah = HapusNomorRumah.next

                    del HapusPemilik
                    del HapusKluster
                    del HapusNamaJalan
                    del HapusBlok
                    del HapusNomorRumah
                elif(HapusPemilik.next is None):
                    self.hapusdatabelakang()
                    print(2)
                else:
                    bantupemilik = self.pemilik
                    bantukluster = self.kluster
                    bantunamajalan = self.nama_jalan
                    bantublok = self.blok
                    bantunomorrumah = self.nomor_rumah

                    while(bantupemilik.next is not HapusPemilik) :
                        bantupemilik = bantupemilik.next
                        bantukluster = bantukluster.next
                        bantunamajalan = bantunamajalan.next
                        bantublok = bantublok.next
                        bantunomorrumah = bantunomorrumah.next

                    bantupemilik.next = HapusPemilik.next
                    bantukluster.next = HapusKluster.next
                    bantunamajalan.next = HapusNamaJalan.next
                    bantublok.next = HapusBlok.next
                    bantunomorrumah = HapusNomorRumah.next
                    del HapusPemilik
                    del HapusKluster
                    del HapusNamaJalan
                    del HapusBlok
                    del HapusNomorRumah
                    input('tekan enter')
                    # HapusPemilik.prev.next = HapusPemilik.next
                    # HapusPemilik.next.prev = HapusPemilik.prev
                    # HapusKluster.prev.next = HapusKluster.next
                    # HapusKluster.next.prev = HapusKluster.prev
                    # HapusNamaJalan.prev.next = HapusNamaJalan.next
                    # HapusNamaJalan.next.prev = HapusNamaJalan.prev

            else:
                print('Data Tidak Ada')
                input('tekan enter')
    
    def UbahData(self) :
        if (self.isEmptypemilik() and self.isEmptykluster() and self.isEmptynamajalan() and self.isEmptyblok() and self.isEmptynomorrumah):
            print('Data Kosong')
        else :
            Ubahpemilik = input('Masukkan Nama Pemilik Yang Ingin Diubah : ')
            bantupemilik = self.pemilik
            bantukluster = self.kluster
            bantunamajalan = self.nama_jalan
            bantublok = self.blok
            bantunomorrumah = self.nomor_rumah
            ketemu = False
            while (not ketemu) and (bantupemilik is not None):
                if (bantupemilik.info == Ubahpemilik) :
                    ketemu = True
                else :
                    bantupemilik = bantupemilik.next
                    bantukluster = bantukluster.next
                    bantunamajalan = bantunamajalan.next
                    bantublok = bantublok.next 
                    bantunomorrumah = bantunomorrumah.next

            if(ketemu) :
                PemilikBaru = input('Masukan Nama Pemilik Baru : ')
                bantupemilik.info = PemilikBaru
            else :
                print('Data Tidak Ditemukan')
    def PencarianData(self) :
        if (self.isEmptypemilik()):
            print("Data Kosong")
        else :
            CariPemilik = input("Masukan Data yang dicari : ")
            bantupemilik = self.pemilik
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantupemilik is not None):
                if (bantupemilik.info == CariPemilik):
                    ketemu = True
                else:
                    bantupemilik = bantupemilik.next
                    posisi = posisi + 1

            if (ketemu):
                pemilik = self.pemilik
                kluster = self.kluster
                nama_jalan = self.nama_jalan
                blok = self.blok
                nomor_rumah = self.nomor_rumah
                print('=================================')
                print('| Pemilik Rumah           :',pemilik.info)
                print('| Kluster                 :',kluster.info)
                print('| Nama Jalan              :',nama_jalan.info)
                print('| Blok                    :',blok.info)
                print('| Nomor Rumah              :',nomor_rumah.info)
                print('=================================')
            else :
                print("Data tidak ditemukan")
            


list1 = Perumahan()
print("=============================================")
print("Menu Aplikasi Data Perumahan LinkedList python |")
print("===============================================|")
print("| 1. Input Data                                |")
print("| 2. Tampilkan Data                            |")
print("| 3. Hapus Data                                |")
print("| 4. Ubah Data                                 |")
print("| 5. Pencarian Data                            |")
print("| 0. Keluar Aplikasi                           |")
print("===============================================|")
pilih = int(input("Masukkan pilihan anda : "))
while pilih != 0:
    if pilih == 1:
        # print('input data')
        DataPemilik = input('Masukkan Pemilik        : ')
        Datakluster = input('Masukkan Kluster        : ')
        Datanamajalan = input('Masukkan Nama Jalan   : ')
        Datablok = input('Masukkan Blok              : ')
        DataNomorRumah = input('Masukan Nomor Rumah   : ')
        list1.inputPemilik(DataPemilik)
        list1.inputKluster(Datakluster)
        list1.inputnamajalan(Datanamajalan)
        list1.inputblok(Datablok)
        list1.inputnomorrumah(DataNomorRumah)

        input("Data Berhasil Ditambahkan, Tekan Enter Untuk Kembali Ke Menu")
    elif pilih == 2:
        list1.TampilData()
    elif pilih == 3:
        list1.TampilData()
        list1.hapusData()
    elif pilih == 4:
        list1.UbahData()
    elif pilih == 5:
        list1.PencarianData()
    elif pilih == 0:
        print('Keluar Aplikasi')
    else:
        print('Pilihan menu tidak ada!')
    print("=============================================")
    print("Menu Aplikasi Data Perumahan LinkedList python |")
    print("=============================================")
    print("| 1. Input Data                             |")
    print("| 2. Tampilkan Data                         |")
    print("| 3. Hapus Data                             |")
    print("| 4. Ubah Data                              |")
    print("| 5. Pencarian Data                         |")
    print("| 0. Keluar Aplikasi                        |")
    print("=============================================")
    pilih = int(input("Masukkan pilihan anda : "))
else:
    print('Thanks')
    list1.PenghancuranPemilik()
   