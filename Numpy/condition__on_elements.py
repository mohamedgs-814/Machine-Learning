import numpy as np

array=np.arange(1,11)
print("---Boolean Condition---")
print("Original Array:",array)
print("Even Array:",array[array%2==0])
print("Number greater than 5:",array[array>5])