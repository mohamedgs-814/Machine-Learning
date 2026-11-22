import numpy as np

#1d array
[1,2,3,4]

#2d array
[
 [1,2,3,4],
 [1,2,5,4]
]

print("2D Matrix\n")
matrix_2D=np.array([[1.0,2,3],[4,5,6],[6,7,8]])
print(matrix_2D)
print(f"Shape: {matrix_2D.shape}")
print(f"Dimension: {matrix_2D.ndim}")
print(f"Size: {matrix_2D.size}")
print(f"Data Type: {matrix_2D.dtype}")


print("3D Matrix\n")
matrix_3D=np.array([
    [[1,2,3],[3,2,1]], #Block 1
    [[4,5,6],[6,5,4]], #Block 2
    [[7,8,9],[9,8,7]]  #Block 3
    ])

print(matrix_3D[0][0][0]) 

print(f"Reshaped given matrix:\n{matrix_3D.reshape(3,3,2)}")
print(matrix_3D) 
print(f"Shape: {matrix_3D.shape}")
print(f"Dimension: {matrix_3D.ndim}")
print(f"Size: {matrix_3D.size}")
print(f"Data Type: {matrix_3D.dtype}")

#Tranpose of matrix_2D
print("tranpose of 2d matrix:\n",np.transpose(matrix_2D))
print("tranpose of 3d matrix:\n",matrix_3D.T)
