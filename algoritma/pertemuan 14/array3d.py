import numpy as np

cube = np.array([
                    [ [1,2,3,],[4,5,6] ],
                    [ [7,8,9],[10,11,12] ]
                ])
for index,elemen in np.ndenumerate(cube):
    print(index,"=>",elemen)
print(cube[1,1,2])
