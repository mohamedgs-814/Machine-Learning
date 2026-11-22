import pandas as pd

data_frame={
    "Name":["Ghouse","Umar"],
    "Age":[19,15],
}

df=pd.DataFrame(data_frame) #General
df=pd.DataFrame(data_frame,index=["Brother 1","Brother 2"]) #My own indexing
print("---Data Frame---")
print(df)

print("\n---Loc property---")
print("Element at index 0:\n",df.loc["Brother 1"])  #Give all the data of a
print()
print("Element at index 1:\n",df.iloc[1])   #Give all the data about person at index 1
print("Loc by shiv:\n",df.loc[df["Character"]=="Good character",["Age","Name"]]),#Returns row in which caharcter =Good character with given columns age and name
print()

#ADDING A NEW COLUMN INTO DATAFRAME

print("\n---Added Column in Data Frame---")
df["Character"]=["Good character","Rude and immuture"]
print(df)

#ADDING A NEW SINGLE ROW INTO DATAFRAME

new_row1=pd.DataFrame([{"Name":"Khadar","Age":48,"Character":"Kind Hearted"}],index=["Father"])
print("\n---Added Row in Data Frame---")

new_df=pd.concat([df,new_row1])
print(new_df)

#ADDING A MULTIPLE ROWS INTO DATABASE
new_row2=pd.DataFrame([{"Name":"Umera","Age":39,"Character":"Soft Hearted"},
                      {"Name":"Honey","Age":8,"Character":"Loyal"}],
                      index=["Mother","Cat"])
print("\n---Added Multiple New Rows Into Data Frame---")
new_df=pd.concat([new_row1,df,new_row2])  #Sequence matters
print(new_df)

#Basic Methods

df["Name"].unique()  #Return the number of unique values present in Name column
df["Name"].nunique() #Return the totall number of unquie values present in Name column
df["Name"].value_counts() #Retuns total number of unquie values and their total occurence