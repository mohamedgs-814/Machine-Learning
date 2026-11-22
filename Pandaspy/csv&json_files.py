import pandas as pd

print("\n---Working with CSV File---")
df=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\students_attendance.csv")
print("\n---CSV Data into Pandas Data Frame---")
print(df)   #Prints only first 5 and last 5 rows

# print(df.to_string())    #Prints complete data frame

print("\n---Working with Json FIle---")
df=pd.read_json(r"D:\Python_AI\MACHINE LEARNING COURSE\students_attendance.json")
print("\n---Json Data into Pandas Data Frame---")
print(df.to_string())
print("Upper Block of df:\n",df.head(10))
print("Lower Block of df:\n",df.tail(10))


#WHAT IF I NEEED ONLY A SPECIFIC COLUMN SUPPOSE IN STUDENT FILE I NEED ONLY NAME OF STUDENTS

print("\n---Single Column---")
print(df["Name"])

print("\n---Only Required Columns---")

print(df[["Name","Marks","Hobby"]])



#WHAT IF I NEED ONLY ROWS
print("---Rows in Data Frame---")
print(df.iloc[0])

    #obviously no one is going to remember index of student rather than student name
        #So pass an argument index_col into dataframe
print("\n---Updated Column name of indexing---")
new_df=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\students_attendance.csv",index_col="Name")
print(new_df)
print(new_df.loc["Varun Rao"])
print()
print(new_df.loc["Aarav Rao",["Marks","Attendance_Percentage"]])



#Producing summary of whole data frame
print("\n---Summary---")
print(df.info())
print(df.describe())