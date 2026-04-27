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


# Average delay per carrier
print("\n3. Mean Departure Delay by Carrier\n")
carriers = df["carrier"].unique()
for c in carriers:
    carrier_delays = df[df["carrier"] == c]["dep_delay"].dropna().values
    mean_delay = round(np.mean(carrier_delays), 2)
    std_delay = round(np.std(carrier_delays), 2)
    print(c, "- Mean:", mean_delay, "\n   - Std Dev:", std_delay)
print()


# Delay stats per airport
print("\n4. Departure Delay Stats by Airport\n")
for origin in df["origin"].unique():
    origin_delays = df[df["origin"] == origin]["dep_delay"].dropna().values
    print(origin)
    print("    Mean:", round(np.mean(origin_delays), 2))
    print("    Median:", round(np.median(origin_delays), 2))
    print("    Std Dev:", round(np.std(origin_delays), 2))
    print("    95th percentile:", np.percentile(origin_delays, 95))
print()


# Delay rates by time of day
print("\n5. Delay Rates by Time of Day\n")
times = ["Morning", "Afternoon", "Evening", "Night"]
for t in times:
    subset = df[df["time_of_day"] == t]
    total = len(subset)
    # is_delayed_depature has a typo in the dataset, keeping it as is
    delayed = np.sum(subset["is_delayed_depature"].values)
    rate = round((delayed / total) * 100, 1)
    mean_delay = round(np.mean(subset["dep_delay"].dropna().values), 2)
    print(t, "- Total:", total, "| Delayed:", delayed, "| Rate:", str(rate) + "%", "| Mean Delay:", mean_delay)
print()


# Outlier detection using IQR
print("\n6. Outlier Detection for Departure Delay (IQR Method)\n")
q1 = np.percentile(dep_delay, 25)
q3 = np.percentile(dep_delay, 75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = dep_delay[(dep_delay < lower) | (dep_delay > upper)]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower bound:", lower)
print("Upper bound:", upper)
print("Number of outliers:", len(outliers))
print("Percentage:", round((len(outliers) / len(dep_delay)) * 100, 2), "%")
print("Worst delay in dataset:", np.max(outliers), "mins")