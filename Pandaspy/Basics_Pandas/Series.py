import pandas as pd

#Series:Series is a one dimensional labeled array that can hold any data type
        #Single Column in spreadsheet

data=[100,202.0,"L",True,not True]
series=pd.Series(data) 
series=pd.Series(data,index=["modified_0","modified_1","modified_2","modified_3","modified_4"]) #my own modified indexing

print("---Series---")
print(type(series)) #Class Pandas Series
print(series)
print("Element at index 2:",series["modified_2"])

#Loc property 
print("\n---LOC Property---")
series.loc["modified_0"]="201", #Modifies exisiting data
print(f"Element accessing using loc with defined index: {series.loc["modified_0"]}")
print(f"Element accessing using iloc with  index: {series.iloc[0]}")


#Filtering data
print("---Filtering data---")
num_data=pd.Series([1,2,3,4,80,99,85,34,5,6,22,1])
print("Filtered Data:\nIndex\tElement\n",num_data[num_data>30])

#Shape and Datatype
print("Shape:",series.shape)
print("Data type:",series.dtypes)