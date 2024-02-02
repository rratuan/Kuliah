# nilai default (default value) jika parameter tidak di isi

# function menuliskan string s sebanyak n kali
def tulis(s = 'Indonesia',n = 1):
    for i in range(1,n+1):
        print(s)

def luasLingkaran(radius, pi = 22/7):
    return pi * radius * radius

# program utama
tulis('Bandung')
tulis('Jakarta',5)
tulis()
print(luasLingkaran(10))
print(luasLingkaran(10,3.14))