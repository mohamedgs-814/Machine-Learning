import numpy as np
a=np.array([10,20,0,30,50,50,53])
print("Array:",a)

#syntax np.where(condition,true output,false output)
required_ind=np.where(a>35) #Give index of elements having num>35

required_val_1=np.where(a>35,1,0) #Gives array of elemnt gretaer than 35
required_val_2=a[required_ind]
print("Indices for condition:",required_ind)
print("True False in array satisfying condition:",required_val_1)
print("Values in array satisfying condition:",required_val_2)