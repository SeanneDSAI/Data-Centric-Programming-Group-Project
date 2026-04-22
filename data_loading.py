import pandas as pd



#uploading the clean data to json and csv files
def upload_clean_data(df, csv_file_name,json_file_name):
    df.to_csv(csv_file_name, index=False)

    df.to_json(json_file_name, orient='split', compression='infer', index=True)
    
    
def clean_data(df):
    """
    Cleans the flights dataframe by removing nulls, duplicates,
    and reformatting the date columns into a single 'date' column.
    """
    #dropping null values
    df = df.dropna()
    
    
    #gets rid of duplicate values 
    df = df.drop_duplicates()
    
    #making new date format 
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']]).dt.strftime('%Y/%m/%d')
    df = df.drop(columns=['year', 'month', 'day', 'time_hour'])
    
    
    return df
    
def data_exploration(df):
    """
    Exploring thdata to find out key inforamtion about it
    """
    print(df.head())
    print(df.info())

def main():
        #loading the raw dataset into a pandas datafram
    try:
        df = pd.read_csv("data/Raw/flights.csv")
    except FileNotFoundError:
        print("Error: flights.csv not found in data/Raw/")



    #getting info about the dataset
    data_exploration(df)
    

    

    og_len = len(df)


    df = clean_data(df)
    #  even by getting rid of all the null values 97% of values still remain

    print(f"{(len(df)/og_len)*100}% of the orginal dataset remains")






    csv_file_name = "data/Processed/flights.csv"
    json_file_name = 'data/Processed/flights.json'

    upload_clean_data(df, csv_file_name, json_file_name)
    
    
if __name__ == "__main__":
    main()