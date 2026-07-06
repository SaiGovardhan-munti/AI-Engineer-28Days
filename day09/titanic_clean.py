import pandas as pd

df = pd.read_csv("titanic.csv")
print(df.isnull().sum())

median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
df = df.dropna(subset=["Embarked"])
female_survivors = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(female_survivors)

survival_rate = df.groupby(["Sex","Pclass"])["Survived"].mean()
print(survival_rate)

df["FareCategory"] = df["Fare"].apply(lambda x: "high" if x > 50 else "low")
print(df[["Fare","FareCategory"]].head(10))



'''
   Output
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
8              9         1       3  ...  11.1333   NaN         S
9             10         1       2  ...  30.0708   NaN         C
..           ...       ...     ...  ...      ...   ...       ...
874          875         1       2  ...  24.0000   NaN         C
875          876         1       3  ...   7.2250   NaN         C
879          880         1       1  ...  83.1583   C50         C
880          881         1       2  ...  26.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S

[231 rows x 12 columns]
Sex     Pclass
female  1         0.967391
        2         0.921053
        3         0.500000
male    1         0.368852
        2         0.157407
        3         0.135447
Name: Survived, dtype: float64
      Fare FareCategory
0   7.2500          Low
1  71.2833         high
2   7.9250          Low
3  53.1000         high
4   8.0500          Low
5   8.4583          Low
6  51.8625         high
7  21.0750          Low
8  11.1333          Low
9  30.0708          Low'''