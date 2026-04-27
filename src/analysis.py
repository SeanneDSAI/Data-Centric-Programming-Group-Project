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
    

# Percentile breakdown for Delays
print("\n2. Percentile Breakdown - Departure / Arrival Delays\n")

dep_delay = df["dep_delay"].dropna().values
arr_delay = df["arr_delay"].dropna().values

percentiles = [10, 25, 50, 75, 90, 95, 99]

print(f"  {'Percentile':<15} {'Dep Delay (mins)':>20} {'Arr Delay (mins)':>20}")
print(f"  {'-'*60}")
for p in percentiles:
    d = np.percentile(dep_delay, p)
    a = np.percentile(arr_delay, p)
    print(f"  {p}th{'':<11} {d:>20.2f} {a:>20.2f}")

# IQR for both
dep_iqr = np.percentile(dep_delay, 75) - np.percentile(dep_delay, 25)
arr_iqr = np.percentile(arr_delay, 75) - np.percentile(arr_delay, 25)
print(f"\n  IQR (Dep Delay):  {dep_iqr:.2f} mins")
print(f"  IQR (Arr Delay):  {arr_iqr:.2f} mins\n")