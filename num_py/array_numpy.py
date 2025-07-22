import numpy as np
arr=np.array([[1,2,3],[4,5,6]]) #2dimessional array

arr2=np.array([1,2,3,4])
print(arr2.dtype)#get the data tyoe of array

arr3=np.array([1.1,2.3,4.5])
arr4=arr3.astype(int)
print(arr4)# change the dat type (arr4=1,2,3,4)

#viem and copy

arr5=arr.copy()
arr[1][0]=88
print("copy",arr5)
print(arr)


arr7 = np.array([[[[1,2,3],[1,2,3],[5,6,7]]]])

#shape
print(arr7.shape) #return (dienssions,lastly_give_the_elments)

arr8=np.array([1,2,3,4],ndmin=5)#create the required numbers of dimmesional array using the nadmin
print(arr8.shape)#(1,1,1,1,4)
