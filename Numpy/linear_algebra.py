import numpy as np

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

print("matrix a:\n",a)
print("matrix b:\n",a)
print()
print()


#Element wise multiplication
print("\nElement-wise multiplication (a*b):")
print(a*b)

#Multiplication of matrix
v1=np.array([1,2,3])
v2=np.array([4,5,6])
print(f"\nDot Product pf vectors {v1} and {v2}: {np.dot(v1,v2)}")


#Matrix operations
matrix=np.array([[1,2],[3,4]])
print("\n---Matrix Properties---")
print(f"Matrix:\n{matrix}")
print(f"Determinant of Matrix:{np.linalg.det(matrix)}")
print(f"Inverse:")
print(np.linalg.inv(matrix))
print(f"Transpose:")
print(matrix.T)

#Eigen Values and Eigen Vectors
eigen_val,eigen_vec=np.linalg.eig(matrix)
print(f"\nEigen Values: {eigen_val}")
print(f"\nEigen Vector: {eigen_vec}")