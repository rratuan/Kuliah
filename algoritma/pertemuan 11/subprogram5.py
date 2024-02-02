def fibo(N):
    if N <= 1:
        return N
    else:
        return fibo(N-2) + fibo(N-1)
    
for i in range(10):
    print(i,' = ',fibo(i))