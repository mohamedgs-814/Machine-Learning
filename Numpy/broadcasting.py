import numpy as np

print("BROADCASTING")
#No map function required in array of numpy
array_01=np.array([10,20,30])
array_01=array_01+12
print("Updated Array",array_01)
print()
print()


#SHAPING RESHAPING CONCEPT
print("Shaping COncept")
array_02=np.array(([[1,2,3,4],[1,2,3,3]]))
array_02=array_02*10

# print(array_02.shape)   #4 rows 1 column output(4,)
# print(array_02.reshape(1,4))    #reshape into 1 row 4 column
# print(array_02.reshape(4,1))    #reshape into 4 row 1 column
# # print(array_02.reshape(5,1))    #reshape into 4 row 1 column,ERROR
# print()
# print()

print(array_02)
print(array_02.reshape(4,2))
print(array_02.shape)
new_array=array_02.reshape(4,2)+array_02.shape
print("New Arrray:",new_array)


#Mean concept and axis=0,axis=1
array_03=np.array([2,4,6,8,30])

new_31=array_03.reshape((5,1))
new_32=array_03.reshape((1,5))
print("Mean of columns",new_31.mean(axis=0)) 
print("Mean of Rows",new_31.mean(axis=1)) 


    #Better understanding
array_04=np.arange(1,13).reshape(4,3)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
 '''
print("Mean of columns",array_04.mean(axis=0)) 
print("Mean of Rows",array_04.mean(axis=1)) #This is 4 rows 1 column
l=[
    [2.],
    [5.],
    [8.],
    [11.]
]
print(np.array(l).shape)

