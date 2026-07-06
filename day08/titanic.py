import pandas as pd

df = pd.read_csv("titanic.csv")
print(df.head())
print(df.info())
print(df.tail())
print(df.describe())
print(df.groupby("Pclass")["Fare"].mean())
