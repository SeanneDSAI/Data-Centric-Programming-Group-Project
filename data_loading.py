import pandas as pd



#uploading the clean data to json and csv files
def upload_clean_data(csv_file_name,json_file_name):
    df.to_csv(csv_file_name, index=False)

    df.to_json(json_file_name, orient='split', compression='infer', index=True)
    
    
def clean_data(df):
    #dropping null values
    df = df.dropna()
    
    
    #gets rid of duplicate values 
    df = df.drop_duplicates()
    
    
    return df
    
#loading the raw dataset into a pandas datafram
df = pd.read_csv("data/Raw/flights.csv")


#getting info about the dataset
print(df.head())
print(df.info())




og_len = len(df)


df = clean_data(df)
#  even by getting rid of all the null values 97% of values still remain

print(f"{(len(df)/og_len)*100}% of the orginal dataset remains")






csv_file_name = "data/Processed/flights.csv"
json_file_name = 'data/Processed/flights.json'

upload_clean_data(csv_file_name, json_file_name)