import pandas as pd
import numpy as np


def get_time_of_day(hour):
    """Returns the time of day category for a given hour."""
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'


def upload_clean_data(df, csv_file_name, json_file_name):
    """Exports the cleaned dataframe to CSV and JSON formats."""
    df.to_csv(csv_file_name, index=False)
    df.to_json(json_file_name, orient='split', compression='infer', index=True)


def merge_companion_data(df):
    """
    Merges the flights dataframe with four companion datasets:
    airlines, airports, weather, and planes.
    """
    # Load companion datasets
    airlines = pd.read_csv('data/Raw/airlines.csv')
    airports = pd.read_csv('data/Raw/airports.csv')
    weather = pd.read_csv('data/Raw/weather.csv')
    planes = pd.read_csv('data/Raw/planes.csv')

    # Merge airlines - adds full airline name
    df = df.merge(airlines, on='carrier', how='left')

    # Merge planes - adds aircraft manufacturer, model, year, engine type
    df = df.merge(planes[['tailnum', 'year', 'manufacturer', 'model', 'engines', 'engine']],
                  on='tailnum', how='left', suffixes=('', '_plane'))

    # Merge airports for origin - adds origin city and coordinates
    airports_origin = airports[['faa', 'name', 'lat', 'lon', 'tzone']].rename(columns={
        'faa': 'origin',
        'name': 'origin_airport_name',
        'lat': 'origin_lat',
        'lon': 'origin_lon',
        'tzone': 'origin_tzone'
    })
    df = df.merge(airports_origin, on='origin', how='left')

    # Merge airports for destination - adds destination city and coordinates
    airports_dest = airports[['faa', 'name', 'lat', 'lon']].rename(columns={
        'faa': 'dest',
        'name': 'dest_airport_name',
        'lat': 'dest_lat',
        'lon': 'dest_lon'
    })
    df = df.merge(airports_dest, on='dest', how='left')

    # Merge weather - adds wind speed, visibility, precipitation etc.
    weather_cols = ['origin', 'month', 'day', 'hour', 'temp', 'wind_speed', 'precip', 'visib']
    df = df.merge(weather[weather_cols], on=['origin', 'month', 'day', 'hour'], how='left')

    print(f"Merged airlines, airports, weather and planes data successfully")
    print(f"Dataset now has {df.shape[1]} columns")
    

    return df


def clean_data(df):
    """
    Cleans the flights dataframe by removing nulls, duplicates,
    and reformatting the date columns into a single 'date' column.
    """
    before = len(df)

    # Drop null values of important subsets
    df = df.dropna(subset=['dep_time', 'arr_time', 'carrier', 'origin', 'dest'])

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Validate data types for numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Remove whitespace from string columns
    df['carrier'] = df['carrier'].str.strip()
    df['origin'] = df['origin'].str.strip()
    df['dest'] = df['dest'].str.strip()

    # Reset index after dropping rows
    df = df.reset_index(drop=True)

    print(f"Dropped {before - len(df)} rows with missing values")

    df = data_engineering(df)
    return df


def data_exploration(df):
    """Prints basic information about the dataframe."""
    print(df.head())
    print(df.info())


def data_engineering(df):
    """
    Engineers new features from existing columns using
    NumPy vectorised operations where possible.
    """
    # Time of day category
    df['time_of_day'] = df['hour'].map(get_time_of_day)

    # Delay flags using NumPy vectorised where
    df['is_delayed_departure'] = np.where(df['dep_delay'] > 0, True, False)
    df['is_delayed_arrival'] = np.where(df['arr_delay'] > 0, True, False)

    # Average speed using vectorised operation
    df['speed'] = np.round(df['distance'] / (df['air_time'] / 60), 2)

    # Delay category
    df['delay_category'] = pd.cut(df['dep_delay'],
                                  bins=[-float('inf'), 0, 15, float('inf')],
                                  labels=['On Time', 'Minor', 'Major'])

    # Aircraft age at time of flight (year column comes from planes merge)
    df['plane_age'] = np.where(df['year_plane'].notna(),
                               2013 - df['year_plane'],
                               np.nan)

    # Weather risk score using NumPy broadcasting-style calculation
    # Normalise wind and visibility into a 0-1 risk score
    if 'wind_speed' in df.columns and 'visib' in df.columns:
        wind_norm = np.clip(df['wind_speed'].fillna(0) / 50, 0, 1)
        visib_norm = np.clip(1 - (df['visib'].fillna(10) / 10), 0, 1)
        df['weather_risk'] = np.round((wind_norm + visib_norm) / 2, 3)



    return df


def main():
    try:
        df = pd.read_csv('data/Raw/flights.csv')
    except FileNotFoundError:
        print("Error: flights.csv not found in data/Raw/")
        return

    og_len = len(df)

    df = merge_companion_data(df)
    df = clean_data(df)
    data_exploration(df)

    print(f"{round((len(df) / og_len) * 100, 2)}% of the original dataset remains")

    # Drop unused columns BEFORE saving to keep file size manageable
    cols_to_drop = [
        'sched_dep_time', 'sched_arr_time', 'flight', 'minute',
        'year_plane', 'engines', 'model',
        'origin_airport_name', 'origin_lat', 'origin_lon', 'origin_tzone',
        'dest_airport_name', 'dest_lat', 'dest_lon',
        'temp', 'precip'
    ]
    df = df.drop(columns=cols_to_drop, errors='ignore')

    csv_file_name = 'data/Processed/flights.csv'
    json_file_name = 'data/Processed/flights.json'

    upload_clean_data(df, csv_file_name, json_file_name)


if __name__ == "__main__":
    main()