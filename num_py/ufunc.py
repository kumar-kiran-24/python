import numpy as np

#create ufunc(universal fuction)
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

def add(a,b):
    return a+b
addfunc=np.frompyfunc(add,2,1)# fuction ,no of intake arguments , no of return arguments
result=addfunc(arr1,arr2)
print(result)