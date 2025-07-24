from numpy import random
import numpy as np
print(random.randint(100,size=5))#generate random numbers of a size is 5 and range to 100
arr1=np.array([1,2,3,4,5])
print(random.choice(arr1))#choose from the randomly in array

#data distribution using random
x=random.choice(arr1,p=[0.1,0.3,0.4,0.2,0],size=5)#p is declare the corrsopnding arrays probality in arr1 for choosing
print(x)