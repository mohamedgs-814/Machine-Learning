import numpy as np

#1D indexing (same as python list)
print("---1D SLICING---")
arr=np.array([1,2,3,4,5])
print("Original Array:",arr)
print("Last Array:",arr[-1])
print("First array:",arr[0])
print("elements 1 to 3:",arr[1:4])
print("Every other element:",arr[::2])

#2D indexing
print("---2D SLICING---")
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n2D Array:")
print(matrix)
print("Element at row 1 column 2:",matrix[1][2],"or",matrix[1,2])
print("First Row:",matrix[0, :]) #matrix[0,start:end]
print("Second column:",matrix[:,1]) #All rows of second column

#3D slicing
print("---3D SLICING---")
matrix_3d=np.arange(1,25.0).reshape(2,3,4) #.reshape(block,row,column)
print("3D Matrix")
print(matrix_3d)

print("Element at (1,1,3):",matrix_3d[1,2,3])
print("First Row:",matrix_3d[0,0,:])

print("Second Column:",matrix_3d[:,:,1].reshape(-1,1))