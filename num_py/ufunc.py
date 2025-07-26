import numpy as np

#create ufunc(universal fuction)
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

def add(a,b):
    return a+b
addfunc=np.frompyfunc(add,2,1)# fuction ,no of intake arguments , no of return arguments
result=addfunc(arr1,arr2)
print(result)
#airthematic universal fuctions
add_=np.add(arr1,arr2)
divide_=np.divide(arr1,arr2)
mul_=np.multiply(arr1,arr2)
sub_=np.subtract(arr1,arr2)

#rounding the decimals in ufuc
arr3= np.trunc([-3.1666, 3.6667])#to remove the decimals return in float

arr4=np.around([3.166,2.6])#increment if decimal greater than 5

#logs
arr5= np.arange(1, 10)
print(np.log2(arr5))#log base 2
print(np.log10(arr5))

#summations
result2=np.sum([arr1,arr2])#sum of the all elements
print(result2)
result3=np.sum([arr1,arr2],axis=1)#return arr1,arr2 sums separtley
result4=np.cumsum([1,2,3,4])#return the sum by next elment with each other from start(0 index) 

#products
result5=np.prod([arr1,arr2],axis=1)#to return the arr1,arr2 mulptiplication of its elemnts

#diffrences
result6=np.diff([arr1])#return the difrence between corrsoponding elments

#LCM and GCD
result7=np.lcm(4,5)
result8=np.gcd(4,5)