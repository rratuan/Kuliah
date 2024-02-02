import numpy as np

data1 = np.array([2,7,9,3,5,1])
data2 = np.array([2,7,9,3,5,1])
data3 = np.array([3,6,7,3,9,2])

print('d1 == d2 : ',np.array_equal(data1,data2))
print('d1 == d3 : ',np.array_equal(data1,data3))
print('d1 > d3 :',np.greater(data1,data3))