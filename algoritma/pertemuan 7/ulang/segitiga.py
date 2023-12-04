n = int(input('N : '))

for i in range(1,n+1):
    segitiga = ' '*(n-i) + '*'*(2*i-1)
    print(segitiga)