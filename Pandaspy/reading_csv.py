import pandas as pd

data_frame=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\data_students.csv")
print(data_frame)


data={
    "Name":["Alice","Bob","Charlie"],
    "Age":["25","48","23"],
    "Country":["USA","Canada","UK"]
}

df=pd.DataFrame(data)
print("\n----Data Frame----\n")
print(df)

#LOADING DATAFRAME

#For csv files
df_csv=pd.read_csv(r"D:\Python_AI\MACHINE LEARNING COURSE\data_students.csv")
#For Excel Spreadsheet
#df=pd.read_excel("monthly_sales_tracker.xlsx"),#ERROR IN THIS EXCEL FILE
print("\n---Data From CSV---\n")
print(df_csv)

#For loading data from dictionar
df=pd.DataFrame(data)