print(' Perhitungan Gaji Karyawan '.center(40,'='))

# input nama pegawai,jabatan,status pernikahan
namaPegawai = input('Nama Pegawai  : ')
jabatan = input('Jabatan       : ').capitalize()
statusPenikahan = input('Menikah [Y/T] : ').upper()

# perhitungan gaji berdasarkan jabatan
if jabatan == 'Direktur':
    gajiPokok = 5000000
elif jabatan == 'Manager':
    gajiPokok = 3000000
elif jabatan == 'Staf':
    gajiPokok = 2000000
else:
    print('Data Tidak Ditemukan')

#deklarasi nilai awal bertujuan untuk memperluas scope agar tidak menimbulkan error di percabangan 
tunjanganKeluarga = 0 #nilai awal tunjangan keluarga
tunjanganAnak = 0 # nialai awal tunjangan anak

# perhitungan tujangan bagi yang menikah
if statusPenikahan == 'Y':
    tunjanganKeluarga = (20/100) * gajiPokok
    banyakAnak = int(input('Banyak Anak : '))
    tunjanganAnak = 10/100
    if banyakAnak == 1:
        tunjanganAnak = tunjanganAnak * gajiPokok
    elif banyakAnak == 2:
        tunjanganAnak = 2 * tunjanganAnak * gajiPokok
    elif banyakAnak == 3:
        tunjanganAnak = 3 * tunjanganAnak * gajiPokok
    else:
        tunjanganAnak = 3 * tunjanganAnak * gajiPokok
elif statusPenikahan == 'T':
    tunjanganKeluarga = 0
    tunjanganAnak = 0

# perhitungan gaji kotor
gajiKotor = gajiPokok + tunjanganKeluarga + tunjanganAnak

# perhitungan pajak
if statusPenikahan == 'Y':
    pajak = (5/100) * gajiKotor
elif statusPenikahan == 'T':
    pajak = (10/100) * gajiKotor

# pendapatan
gajiBersih = gajiKotor - pajak

# output
print('=' * 40)
print(f'''Gaji Pokok         : Rp. {gajiPokok:9.0f}
Tunjangan Keluarga : Rp. {tunjanganKeluarga:9.0f}
Tunjangan Anak     : Rp. {tunjanganAnak:9.0f}
Gaji Kotor         : Rp. {gajiKotor:9.0f}
Pajak              : Rp. {pajak:9.0f}
Gaji Bersih        : Rp. {gajiBersih:9.0f}''')