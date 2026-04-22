import pandas as pd



df = pd.read_csv("data/Raw/flights.csv")

csv_file_name = "data/Processed/flights.csv"
json_file_name = 'data/Processed/flights.json'

print(df.head())

print(df.info())

og_len = len(df)
df = df.dropna()
#  even by getting rid of all the null values 97% of values still remain

print(len(df)/og_len)



df.to_csv(csv_file_name, index=False)

df.to_json(json_file_name, orient='split', compression='infer', index=True)