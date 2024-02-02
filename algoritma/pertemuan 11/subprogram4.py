def faktorial(N):
    if N > 1: #kondisi rekursif
        return N * faktorial(N-1)
    else: #kondisi base case
        return 1

def faktorial2(N): #pake loop
    hasil = 1
    for i in range(2,N+1):
        hasil = hasil * i
    return hasil

print(faktorial(1))
print(faktorial(2))
print(faktorial(5))

print(faktorial2(5))