import random

data_asli = [random.randint(1,100) for i in range(20)]
print('Data asli :',data_asli)

data_terurut = sorted(data_asli)
print('Data terurut :',data_terurut)

data_terbalik = sorted(data_asli,reverse=True)
print('Data terurut terbalik :',data_terbalik)

def getSatuan(angka):
    return angka % 10

terurut_satuan = sorted(data_asli,key=getSatuan)
print('Data terurut satuan :',terurut_satuan)