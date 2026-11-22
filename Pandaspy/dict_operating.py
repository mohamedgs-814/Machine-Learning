import pandas as pd

calories={
    "Day1":1750,
    "Day2":2100,
    "Day3":1700
}

print("---Dictionary Series---")
series=pd.Series(calories)
print(series)

print("---Log property---")
print(series["Day1"])
print(series["Day1"])

print("---Updating Values---")
print("Day3 before updating:",series["Day3"])
series.loc["Day3"]+=300
print("Day3 after updating:",series["Day3"])

