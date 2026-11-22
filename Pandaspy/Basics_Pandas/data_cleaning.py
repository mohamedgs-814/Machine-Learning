import pandas as pd

"""
Data Cleaning= The processs of fic=xing/removing
                incomplete, incorrect, or irrelevant data.
                ~75% of work with Oandas is data cleaning
"""

df=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\data_students.csv")

# print(df.to_string())

df=df.drop(columns=["Roll_Number","Gender"])

print(df.to_string())

#Suppose there are no values for specifc column in few rows 
#To clean data i.e to remove the rows which do not have data for column
df=df.dropna(subset=["Age"])        #drop not available dropna

print(df.to_string())

#Instead of removing row with no data for specific column fill with something else
df=df.fillna({"Name":"Replaced"})

#Standardize text

print("---Names chnaged to Upper cases---")
df["Name"]=df["Name"].str.upper()
print(df)

#Fix data type,i.e chnaging data type

print("---Changed the Student ID into int type")
df["Student_ID"]=df["Student_ID"].astype(bytes)
print(df)

#Remove duplicate function
print("---Deleting Duplicates---")
print(df)
df=df.drop_duplicates()

print(df.to_string())

