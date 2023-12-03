#Menentukan Gaji Karyawan
#I.F : Memasukan NIK,Nama Karyawan,Golongan dan Jumlah Jam Kerja
#F.S : program mengeluarkan NIK,Nama Karyawan, Gaji Pokok, Tunjangan, Lembur,
print("="*32)
print("Program Penghitung Gaji Karyawan")
print("="*32)
nik = str(input("Nomor Induk Karyawan   : "))
namakaryawan = str(input("Nama Karyawan :   "))
gol = str(input("golongan   :   "))

if  (gol=="1") or (gol=="2"):
    JumlahJamKerja = int(input("Jumlah Jam Kerja/bulan  :   "))

    #Menentukan Gaji Pokok dan Tunjangan
    if gol == "1" :
        gajipokok = 1750000
        tunjangan = 0.125 * gajipokok
        besartunjangan = "12.5%"
    else :
        gajipokok = 2300000
        tunjangan = 0.15 * gajipokok
        besartunjangan = "15%"
    #Menentukan Uang Lembur atau Potongan Gaji
    if JumlahJamKerja > 208 :
        jamlembur = (JumlahJamKerja - 208)
        lembur = jamlembur * 25000
        potongan = 0
        haritidakkerja = 0
        jamtidakkerja = 0
    else :
        lembur = 0
        haritidakkerja = ((208 - jumlahjamkerja) // 8)
        jamtidakkerja = ((208 - jumlahjamkerja) % 8)
        potongan1 = haritidakkerja * 50000
        porongan2 = jamtidakkerja * 10000
        potongan = potongan1 + potongan2
    #Menghitung Gaji Bersih yang Didapat
    gajibersih = (gajipokok + tunjangan + lembur) - potongan

    #Output yang didapat
    print("="*30)
    print("Rincian Yang di Terima")
    print(""*30)
    print("Nomor Induk Karyawan : ",nik)
    print("Nama Karyawan        : ",namakaryawan)
    print("Golongan             : ",gol)
    print("Jumlah Jam Kerja     : ",jumlahjamkerja , "jam")
    print("="*30)
    print("Gaji pokok           :", gajipokok)
    print("Tunjangan ",besartunjangan,"     : Rp. ", tunjangan)
    if lembur > 0 :
        print("Lembur          : ", jamlembur,"jam")
        print("                : Rp. ",lembur)
        print("Gaji Bersih     : Rp. ",gajibersih)
    elif potongan > 0 :
        print("Potongan        : -" , haritidakkerja, "hari",jamtidakkerja,"jam")
        print("                : Rp. ",potongan)
        print("Gaji Bersih     : Rp. ",gajibersih)
        print("Gaji Bersih     : Rp. ",gajibersih)
    else:
        print("!!!!!Golongan Salah!!!!!")
        print("     Silahkan Muat Ulang Program     ")

    