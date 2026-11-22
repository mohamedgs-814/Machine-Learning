import pandas as pd
#Aggregate functions=reduces a set of values into a single summary value
#                    used to summarize and analyse data
#                    Often udes with the groupvy() function

df=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\students_attendance.csv")

#I cannot get mean of column of which is alphabetical
"""print(df.mean()) Mean of data frame fails for data with alphabets"""



#Aggregate function for whole database
print("\nAggregate Function on Whole database\n")
print("---Average of columns with numeric Values---")
print(df.mean(numeric_only=True)) #Aggertae funtion

print("\n---Sum of numeric values from each row---")
print(df.sum(numeric_only=True))

print("\n---Minimum numeric value from each column in data frame---")
print(df.min(numeric_only=True))

print("\n---Max numeric value from each column in data fram---")
print(df.max())




#Aggreate function for single column
print("\nAggregate Function on Column\n")
print("\n---Average of Attendance Column---")
print("Mean of Attendance:",df["Attendance_Percentage"].mean()) #Aggertae funtion

print("\n---Sum of numeric values from each row---")
print("Total marks scored by all students:",df["Marks"].sum(numeric_only=True))

print("\n---Minimum numeric value from each column in data frame---")
print("Least Attendance:",df["Attendance_Percentage"].min(numeric_only=True))

print("\n---Max numeric value from each column in data fram---")
print("Highest Attendance:",df["Attendance_Percentage"].max())


