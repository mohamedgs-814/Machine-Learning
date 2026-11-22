import numpy as np

zero_array=np.zeros(5) #[0. 0. 0. 0. 0.] ,default is float for int use dtype=np.int inside zeros function


rows_columns=np.ones((2,5)) #ROWS of 2 and COLOUMS of 5
"""Output for above variable
[
    [1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]
]"""


lin_space=np.linspace(0,4,6)  #6 elements evenly spaced 0 to ,i.e increment evenly ,[0.  0.8 1.6 2.4 3.2 4. ]
print(*lin_space)