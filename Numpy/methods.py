import numpy as np

#01_linspace-evenly spaced numbers
array_01=np.linspace(2,19,6) #Start,stop, number of elements, EVENLY INCREMENT THE VALUE OF NEXT ELEMNT BY DIFFERENCE OF FIRST TWO
print("np.linspace()",array_01) #2 to 19 total number of elemts is array should be 6
for element in array_01:
    print(element,"Type:",type(element))
    #Elements can be int float etc

#02_Creating arrays of zero
zeros=np.zeros((5,3),int) #number of zeros required
print("Zeros",zeros)

#03_Creating arrays of ones
ones=np.ones(5) #number of ones required

#04_Creating arrays with a specific value
full=np.full(6,9)  #six elements with value 9
print("Full 6E with 9V",full)

#05_indentity matrix
identity=np.eye(7) #Identity square matix of 7X7
print("Identity matrix:\n",identity)


#06_Random arrays
random_arr=np.random.rand(4)
print("Random:",random_arr)

random_int=np.random.randint(1,10,size=7) #start with 1 excluding 10 with number of elements 7
print("Random integers:",random_int)