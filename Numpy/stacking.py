import numpy as np

a=np.array([1,2,3])
b=np.array([5,6,7])
c=np.array([0,6,7])

print("Array 1:",a)
print("Array 2:",b)

print("---STACKING---")
print("Vertical Stacking:\n",np.vstack((a,b,c)))
print("Horizontal Stacking:\n",np.hstack((a,c,b)))
print("Stack as columns:\n",np.column_stack((a,c,b)))