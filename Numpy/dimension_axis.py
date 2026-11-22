import numpy as np

# matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("Matrix:\n")
# print(matrix)
# print("Shape:",matrix.shape)
# print()
# print()

# #axis=0: collapse rows (opertes down the column)-> one value per column
# sum_axis0=np.sum(matrix,axis=0)
# print(f"axis=0 (down rows):{sum_axis0} -> shape:{sum_axis0.shape}")  #return a matrix by adding all columns present and the postion
# #of the result is row0 column same as the column on which operation is performed
# print(f" Example: column 0 sum:{matrix[0,0]}+{matrix[1,0]}+{matrix[2,0]}={sum_axis0[0]}")
# #axis=0: collapse (operates across rows) -> one value per row
# sum_axis1=np.sum(matrix,axis=1)
# print(f"axis=1 (across column): {sum_axis1} -> Shape: {sum_axis1.shape}")
# print(f" Example: row 0 sum:{matrix[0,1]}+{matrix[0,2]}+{matrix[0,2]}={sum_axis1[0]}")


#Thinking for 3-d (depth,row,column)
print("---3D dimensional Array")

matrix3=np.array([
    [
    [1,2,3],
    [4,5,6]
    ],
    [
    [7,8,9],
    [10,11,12]
    ]
])

print("3D Array (shape:2X2X3):")
print("Think: 2 blocks,each with 2X3 matrix")
print(matrix3)
print(f"Shape: {matrix3.shape} (block=2,row=2,columns=3)\n")

#axis=0: collapse depth (across pages) -> result: 2D (2X3)
axis0=np.sum(matrix3,axis=0)
print(f"axis=0 (across pages):\n{axis0} -> shape: {axis0.shape}")
print(f" Example: [0,0,0] = {matrix3[0,0,0]}+{matrix3[1,0,0]} = {axis0[0,0]}\n")

#axis1 and axis2 are same as axis0 and axis 1 in 2-D matrix