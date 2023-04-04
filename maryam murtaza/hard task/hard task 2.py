             #Task 2

import numpy as np
list_1=np.array([3,2,0,1])
print(np.sort(list_1))
list_2=np.array([7,6,8])
print(np.sort(list_2))
list_3=np.concatenate((list_1,list_2))
print(np.sort(list_3))
x=np.median(list_3)
print(x)
