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

arr8=np.array([1,2,3,4,5,6],ndmin=5)#create the required numbers of dimmesional array using the nadmin
print(arr8.shape)#(1,1,1,1,4)

#array reshape
arr9=np.array([1,2,3,4,5,6])
arr10=arr9.reshape(2,3)#dimesions,elments
print(arr10)

#joining array
arr11=np.array([1,2,3,4,5,6])
arr12 = np.concatenate((arr9, arr11))
print(arr12)

#array serach
w=np.where(arr12==2)
print(w)
# find even values index using where method
print(np.where(arr%2 == 1))

#sorted search
print(np.searchsorted(arr12,1)) 
print(np.searchsorted(arr12,1,"right"))#serch from last index

#sorting the array
arr13=np.sort(arr12)
print(arr13)

#filtering array
filter_arr=[]
for n in arr12:
    if n>3:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
arr14=arr12[filter_arr]
print(arr14)
