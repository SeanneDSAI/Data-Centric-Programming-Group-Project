import pandas as pd
import numpy as np

def get_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'


#uploading the clean data to json and csv files
def upload_clean_data(df, csv_file_name,json_file_name):
    df.to_csv(csv_file_name, index=False)

    df.to_json(json_file_name, orient='split', compression='infer', index=True)
    
    
def clean_data(df):
    """
    Cleans the flights dataframe by removing nulls, duplicates,
    and reformatting the date columns into a single 'date' column.
    """
    
    before = len(df)
    #dropping null values of important subsets
    df = df.dropna(subset=['dep_time', 'arr_time', 'carrier', 'origin', 'dest'])
    
    
    #gets rid of duplicate values if any
    df = df.drop_duplicates()
    
    
    #validating the data types for numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    #removing whitespace from string columns
    df['carrier'] = df['carrier'].str.strip()
    df['origin'] = df['origin'].str.strip()
    df['dest'] = df['dest'].str.strip()
    
    #reseting index of dropped rows
    df = df.reset_index(drop=True)
    
    print(f"Dropped {before - len(df)} rows with missing values")
    
    df = data_engineering(df)
    return df
    
def data_exploration(df):
    """
    Exploring thdata to find out key inforamtion about it
    """
    print(df.head())
    print(df.info())
    
    
def data_engineering(df):
    #getting the time of dat the plane 
    df['time_of_day'] = df['hour'].map(get_time_of_day)
    
    #plane is delayed leaving the airport
    df['is_delayed_depature'] = df['dep_delay'] > 0
    
    #see if the plane is delayed arriving at the airport
    df['is_delayed_arrival'] = df['arr_delay'] > 0
    
    # calcualting the average speed of the plane
    df['speed'] = df['distance']/(df['air_time']/ 60).round(2)
    
    df['delay_category'] = pd.cut(df['dep_delay'],
    bins=[-float('inf'), 0, 15, float('inf')],
    labels=['On Time', 'Minor', 'Major'])
    
    #making new date format, time hour was accurate
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']]).dt.strftime('%Y/%m/%d')
    df = df.drop(columns=['year', 'month', 'day', 'time_hour'])
    
    return df

def main():
        #loading the raw dataset into a pandas datafram
    try:
        df = pd.read_csv("data/Raw/flights.csv")
    except FileNotFoundError:
        print("Error: flights.csv not found in data/Raw/")



    #getting info about the dataset

    og_len = len(df)


    df = clean_data(df)
    data_exploration(df)
    #  even by getting rid of all the null values 97% of values still remain

    print(f"{(len(df)/og_len)*100}% of the orginal dataset remains")

    csv_file_name = "data/Processed/flights.csv"
    json_file_name = 'data/Processed/flights.json'

    upload_clean_data(df, csv_file_name, json_file_name)
    
    
if __name__ == "__main__":
    main()