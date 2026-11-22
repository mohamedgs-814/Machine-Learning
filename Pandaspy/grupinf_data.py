import pandas as pd

df=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\students_attendance.csv")


#Creates a multiple group like in hobby group1=cricket group 2=dancing group 3=football gaming
group=df.groupby("Hobby")

print("---Mean of marks scored by students in each group---")
print(group["Marks"].mean()) #Return mean of marks of each group with their names

print("--Max marks scored by student in each group---")
print(group["Marks"].max())  #Return maximum marks scored by student in their prespective group

