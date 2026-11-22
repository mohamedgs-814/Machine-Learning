import numpy as np
import time
l=[1,23,3]

print(l)    #List
print(np.array(l))   #array of numpy
print(*np.array(l),sep="--> ")    #iterated array


print(f"Numpy version {np.__version__}")
print()
print()

#   comparing the net speed/efficieny/difference between python list and numpy array

#Performing operation on python list
t1=time.time()
num_list=list(range(10000000))
num_list_sum=sum(num_list)
print(f"Calculating Sum of elements present in  num_list")
print("Sum of elements in num_list",num_list_sum,"\nTime taken:",round(time.time()-t1,5))
print()
print()
#Performing operation on numpy array
t2=time.time()
num_array=np.arange(10000000)
num_array_sum=num_array.sum()
print("Calculating Sum of elements present in num_array")
print("Sum of elements in num_array",num_array_sum,"\nTime taken:",round(time.time()-t2,5))
print()
print()