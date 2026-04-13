import pandas as pd


df = pd.read_csv("flights.csv")

print(df.head())

print(df.info())

og_len = len(df)
df = df.dropna()
#  even by getting rid of all the null values 97% of values still remain

print(len(df)/og_len)