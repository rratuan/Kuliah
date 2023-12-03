Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 12
b = 7
c = a + b
c
19
type(a+b)
<class 'int'>
type(a-b)
<class 'int'>
type(a/b)
<class 'float'>
type(a//b)
<class 'int'>
type(a**b)
<class 'int'>
type(6/3)
<class 'float'>
a > b
True
b > a
False
a == b
False
a != b
True
type(a//b)
<class 'int'>








a = 6.7
aa
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    aa
NameError: name 'aa' is not defined. Did you mean: 'a'?
a = 2e12
a
2000000000000.0
2.5e12
2500000000000.0
5.5 ** 2
30.25
5.5 ** 2.5
70.94253836732938


s = 'Bandung Kota Kembang'
type(s)
<class 'str'>
s = """Bandung Kota Kembang
Bandung Lautan Api"""
s
'Bandung Kota Kembang\nBandung Lautan Api'
namadepan = 'asep'
namabelakang = 'suptiatna'
nama lengkap = namadepan + ' ' + namabelakang
SyntaxError: invalid syntax
namalengkap = namadepan + ' ' + namabelakang
nama lengkap
SyntaxError: incomplete input
namalengkap
'asep suptiatna'
print(namalengkap)
asep suptiatna
ulang = namadepan * 6
print(ulang)
asepasepasepasepasepasep




namadepan.upper()
'ASEP'
namadepan = namadepan.upper()
namadepa
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    namadepa
NameError: name 'namadepa' is not defined. Did you mean: 'namadepan'?
namadepan
'ASEP'
namadepan.lower()
'asep'
namadepan.capitalize()
'Asep'
namabelakang.replace('a','o')
'suptiotno'
'suptiotno'
'suptiotno'

namabelakang.find('r')
-1
namabelakang.find('p')
2
alfa = 'ABCDEFGHIJKLMNO'
alfa
'ABCDEFGHIJKLMNO'
alfa[0]
'A'
alfa[5]
'F'
alfa[10]
'K'
alfa[-1]
'O'
alfa[0:5]
'ABCDE'
alfa[5:8]
'FGH'
alfa[2::2]
'CEGIKMO'
alfa[:10:3]
'ADGJ'
alfa[0].replace('Z')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    alfa[0].replace('Z')
TypeError: replace expected at least 2 arguments, got 1
alfa = alfa[0].replace('Z')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    alfa = alfa[0].replace('Z')
TypeError: replace expected at least 2 arguments, got 1
alfa.replace([0],'Z')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    alfa.replace([0],'Z')
TypeError: replace() argument 1 must be str, not list
alfa[:1] +'z'+alfa[2:]
'AzCDEFGHIJKLMNO'
nama = 'Budi Permana'
namaDepan = nama[0:5]
namaDepan
'Budi '
nama = 'Andri Heryandi'
nama[0:nama.find(' ')]
'Andri'
nama[nama.find(' '):]
' Heryandi'
nama = 'Ratuayu Nurfajar Kamaludin'
nama[nama.find(' '):]
' Nurfajar Kamaludin'
nama[nama.find(' '):[-1]]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    nama[nama.find(' '):[-1]]
TypeError: slice indices must be integers or None or have an __index__ method
nama[-1][0]
'n'
nama[nama.find(' '):-1]
' Nurfajar Kamaludi'
nama[nama.find(''):0]
''
nama[0:nama.find(' '):-1]
''
nama
'Ratuayu Nurfajar Kamaludin'
' Nurfajar Kamaludi'
' Nurfajar Kamaludi'


nama[:-1:nama.find(' ')]
'R al'
nama[nama.find(' '):-1]
' Nurfajar Kamaludi'




nama[0]
'R'
nama[-1]
'n'
nama[-1:]
'n'
nama[:]
'Ratuayu Nurfajar Kamaludin'
nama[::]
'Ratuayu Nurfajar Kamaludin'
nama[:-1]
'Ratuayu Nurfajar Kamaludi'
nama[:-1:0]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    nama[:-1:0]
ValueError: slice step cannot be zero
nama[-1:0]
''
nama[-1:1]
''
gabung = 'naik vespa keliling kota'
pisah = gabung.split()
print(pisah)
['naik', 'vespa', 'keliling', 'kota']

pisah = gabung.split('=')
print(pisah)
['naik vespa keliling kota']
pisah = gabung.split()

print(pisah)
['naik', 'vespa', 'keliling', 'kota']
join = pisah.join()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    join = pisah.join()
AttributeError: 'list' object has no attribute 'join'
join = 'iya'.join(pisah)
print(join)
naikiyavespaiyakelilingiyakota
>>> pisah = join.split()
>>> print(pisah)
['naikiyavespaiyakelilingiyakota']
>>> pisah = join.split('iya')
>>> print(pisah)
['naik', 'vespa', 'keliling', 'kota']
>>> nama
'Ratuayu Nurfajar Kamaludin'
>>> nama[nama.split():-1]
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    nama[nama.split():-1]
TypeError: slice indices must be integers or None or have an __index__ method
>>> nama[:nama.split([-1])
... q
...      
SyntaxError: incomplete input
>>> nama[:nama.split([-1])]
...      
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    nama[:nama.split([-1])]
TypeError: must be str or None, not list
