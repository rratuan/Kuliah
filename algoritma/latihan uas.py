# import random

# for i in range(1,3):
#     print(random.randint(1,5), end=' ')


# for i in range(1,12,2):
#     print(i)

# data1 = [5,7,3,5,3,6]
# print(data1)


data2 = [['adi',80],
        ['budi',85],
        ['cecep',58],
        ['dede',85],
        ['encep',68]
        ]
n = len(data2)

def sortData(x):
    for i in range(n):
        idx = i
        for j in range(i+1,n):
            if x[j][1] > x[idx][1]:
                idx = j
        x[i],x[idx] = x[idx],x[i]

sortData(data2)
print(data2)
        