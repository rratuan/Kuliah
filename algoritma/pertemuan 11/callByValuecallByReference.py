Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
id(a)
2221740261904
a = a + 3
a
13
id(a)
2221740262000
b =2.5
id (b)
2221745666096
b = 5.8
id(b)
2221776019632
s = 'abc'
id(s)
2221741546800
s = 'def'
id (s)
2221742169520
2221740262000
2221740262000



>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> data = []
>>> id(data)
2221777452672
>>> data.append(10)
>>> id(data)
2221777452672
>>> data.append(20)
>>> data
[10, 20]
>>> id(data)
2221777452672
>>> data[0] = 50
>>> data
[50, 20]
>>> id(data)
2221777452672
