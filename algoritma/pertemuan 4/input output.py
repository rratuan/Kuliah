Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = input()
Bandung
a
'Bandung'
a = input("Nilai A : ")
Nilai A : 50

a
'50'
b = int(input("Nilai B : "))
Nilai B : 10
b
10
type(a)
<class 'str'>
type(b)
<class 'int'>
a = int(a)
a
50
c = a + b
c
60
type(c)
<class 'int'>
st_c = str(c)
c
60
st_c
'60'
type(st_c)
<class 'str'>

a = 12345
b = 6789.123
c = "kota bandung"
print(a)
12345
print(b)
6789.123
print(c)
kota bandung
print(a,b,c)
12345 6789.123 kota bandung
print('Data :',a,b,c)
Data : 12345 6789.123 kota bandung
print(a,b,c,sep='-')
12345-6789.123-kota bandung
print('Data:',a,b,c,sep=' kemudian ')
Data: kemudian 12345 kemudian 6789.123 kemudian kota bandung
print(a,b,c,sep='\n')
12345
6789.123
kota bandung
print('Baris 1');print('Baris 2');print('Baris 3')
Baris 1
Baris 2
Baris 3
print('Baris 1',end='');print('Baris 2');print('Baris 3')
Baris 1Baris 2
Baris 3
print('Baris 1',end='\n\n');print('Baris 2')
Baris 1

Baris 2
print(a,b,c,sep='x',end='\n\n')
12345x6789.123xkota bandung

print('Nilai A : %i, B : %f, C : %s' % (a,b,c))
Nilai A : 12345, B : 6789.123000, C : kota bandung
a = 12345
print('A : %i', % a)
SyntaxError: invalid syntax
print('A : %i' % a)
A : 12345
print('A : %10i' % a)
A :      12345
print('A : %010i' % a)
A : 0000012345
print('A " %+10i' % a)
A "     +12345
print('%s %i' % (c,a))
kota bandung 12345
print('%-30s %i' % (c,a))
kota bandung                   12345
print('%30s %i' % (c,a))
                  kota bandung 12345
b = 123.45678
print(b)
123.45678
print('%f' % b)
123.456780
print('%20f' % b)
          123.456780

print('%20.2f' % b)
              123.46
print('A : {}, B : {}, C : {}'.format (a,b,c))
A : 12345, B : 123.45678, C : kota bandung
tgl = 13
bln = 06
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
bln = 6
thn = 2005
print('{}-{}-{}'.format (tgl,bln,thn))
13-6-2005
print('{1}-{0}-{}2'.format (tgl,bln,thn))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print('{1}-{0}-{}2'.format (tgl,bln,thn))
ValueError: cannot switch from manual field specification to automatic field numbering
>>> print('{1}-{0}-{2}'.format (tgl,bln,thn))
6-13-2005
>>> print('{2}-{1}-{0}'.format (tgl,bln,thn))
2005-6-13
>>> print('{}-{}-{}'.format (thn,bln,tgl))
2005-6-13
>>> print('[{:30}]'.format ('bandung'))
[bandung                       ]
>>> print('[{:>30}]'.format ('bandung'))
[                       bandung]
>>> print('[{:^30}]'.format ('bandung'))
[           bandung            ]
>>> print(f'A : {a}, B : {b}, C : {c}')
A : 12345, B : 123.45678, C : kota bandung
>>> print(f'A : {a:10}, \nB : {b:13.2f}')
A :      12345, 
B :        123.46
>>> print(f'A : {a:10} \nB : {b:13.2f}')
A :      12345 
B :        123.46
