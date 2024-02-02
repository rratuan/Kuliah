M = int(input('M : '))
N = int(input('N : '))

def penjumlahan(M,N):
    hasilLokal = 0
    for i in range(M):
        hasilLokal += N
    print(f'{M} x {N} =',end= " ")
    for i in range(M):
        if i == M-1:
            print(N, end=" ")
        else:
            print(N, '+', end= " ")
    print('=',hasilLokal)
    return(hasilLokal)

penjumlahan(M,N)