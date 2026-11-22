import pandas as pd

df=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\students_raw.csv")


print("---Question 2---")
print("Shape:",df.shape)
print("Info:\n")
df.info()
print("describing Data:\n")
print(df.describe())
print()
print(df.head())


print("\n---Question 3---")

print("Students who studied  more than 7 hours:")
print("Total Number of students:",(df["hours_studied"]>7).sum())
print("Student with highest stuty time:",(df["hours_studied"].max()))
# print(df.to_string())
print("Dropped missing values in hours studied")

print("Total Number of empty space in data:\n",df.isna().sum())
print((df.dropna(subset=["hours_studied"])))

print("\n---Taking column out of data and getting its type---")
print(type(df["previous_score"]).__name__)


print("---Getting First Three Column of Data Frame with Student_id and name---")
print(df.loc[0:3,["student_id","name"]])