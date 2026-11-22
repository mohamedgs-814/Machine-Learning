import numpy as np

array_1=np.arange(1,11).reshape(5,2)
array_2=np.arange(10,0,-1).reshape(5,2)


print("---Concatenation---")
print("Array 1:",array_1)
print("Array 2:",array_2)

print("---Vertical concatenation  vstack(a,b)---")
print("Vertical stack:\n",np.vstack((array_1,array_2)))
print()

print("---Horizontal concatenation  hstack(a,b)---")
print("Horizontal stack:\n",np.hstack((array_1,array_2)))

print("\n---Using Concatenate---")
print("Vertical Concatenate:",np.concatenate((array_1,array_2),axis=0))
print("Horizontal Concatenate:\n",np.concatenate((array_1,array_2),axis=1))
      