import numpy as np

def my_sum(data):
    total = 0
    for elemen in data:
        total = total + elemen
    return total

def my_mean(data):
    return my_sum(data)/len(data)

def my_str(x):
    rataRata = my_mean(x)
    total = 0 
    for i in range(len(x)):
        total = total + (x[i] - rataRata)**2
    return (total/(len(x)-1))**0.5

# testing
nilai = [67,48,90,75,43]
print("Sum : ",my_sum(nilai),"-->",np.sum(nilai))
print("Rata-Rata : ",my_mean(nilai),"-->",np.mean(nilai))
print('Std Dev : ',my_str(nilai),"-->",np.std(nilai,ddof=1))