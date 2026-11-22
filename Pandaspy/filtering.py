import pandas as pd

df=pd.read_json(r"D:\Python_AI\MACHINE LEARNING COURSE\students_attendance.json")

print("---Filtering Column in Data Frame---")
attendence_const=df[df["Attendance_Percentage"]>=85]

print("\nFiltered Students with Attendence >=85%")
print(attendence_const)

print("\nFiltering Students with marks>90 or attendence>=85:")
eligible_student=df[(df["Marks"]>90) | (df["Attendance_Percentage"]>=85)]   # | or operator in pandas
print(eligible_student)

print("\nFiltering Students with marks>90 and attendence>=85")
eligible_sem=df[(df["Marks"]>90) & (df["Attendance_Percentage"]>=85)]  # & operator in pandas
print(eligible_sem)

