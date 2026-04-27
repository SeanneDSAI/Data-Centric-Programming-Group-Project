import numpy as np
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('data/Processed/flights.csv')

# Prints size of dataset
print("\nDataset has", df.shape[0], "rows and", df.shape[1], "columns")
print()


# Descriptive Stats function
def summarise_column(arr, label):
    """
    Prints important NumPy stats for a numeric array.
    """
    arr = arr[~np.isnan(arr)]  # drop NaNs before calculating
    print(f"  {label}")
    print(f"    Mean:       {np.mean(arr):.2f}")
    print(f"    Median:     {np.median(arr):.2f}")
    print(f"    Std Dev:    {np.std(arr):.2f}")
    print(f"    Variance:   {np.var(arr):.2f}")
    print(f"    Min:        {np.min(arr):.2f}")
    print(f"    Max:        {np.max(arr):.2f}")
    print()

print("1. Descriptive Stats (NumPy)\n")

numeric_cols = {
    "Departure Delay (mins)": df["dep_delay"].values,
    "Arrival Delay (mins)":   df["arr_delay"].values,
    "Air Time (mins)":        df["air_time"].values,
    "Distance (miles)":       df["distance"].values,
    "Speed (mph)":            df["speed"].values,
}

for label, arr in numeric_cols.items():
    summarise_column(arr, label)