# Flight Delay Analysis – NYC 2013

Exploring flight delays from New York City airports (JFK, LGA, EWR) across 336,000 flights in 2013.
We investigate which airlines are most delayed, how delays vary by time of day and month, and which routes are busiest — using the `nycflights13` dataset.

---

## Team Members

| Name | Role | Responsibilities |
|------|------|-----------------|
| **Dillon** | Data Engineer | Loading and cleaning data, handling missing values, preparing the dataset |
| **Jack** | Data Analyst | Calculating average delays, finding patterns, extracting insights |
| **Oluwadamise** | Visualization Lead | Creating charts and graphs to communicate findings |
| **Seanne** | Documentation Lead | Managing the repo and branching strategy, writing the README, building the end-to-end Jupyter notebook, adding docstrings and inline comments throughout the codebase, and defining the project folder structure |

---

## Dataset Source

Data is sourced from the [`nycflights13`](https://github.com/tidyverse/nycflights13) R package (tidyverse), loaded directly from GitHub raw CSV files. It covers all flights departing NYC airports (JFK, LGA, EWR) in 2013, along with four companion datasets:

| File | Description |
|------|-------------|
| `flights.csv` | 336,776 flight records — the primary dataset |
| `airlines.csv` | Full airline names mapped to carrier codes |
| `airports.csv` | Airport metadata including coordinates and timezone |
| `weather.csv` | Hourly weather readings per origin airport |
| `planes.csv` | Aircraft metadata (manufacturer, model, engine type) |

---

## Project Structure

```
flight-analysis/
├── data/
│   ├── Raw/                  # Original CSVs downloaded from source
│   └── Processed/            # Cleaned and merged dataset (flights.csv, flights.json)
├── src/
│   ├── pre_data_loading.py   # Stage 1: Downloads raw CSVs from GitHub
│   ├── data_loading.py       # Stage 2: Merges, cleans, and engineers features
│   ├── analysis.py           # Stage 3: Statistical analysis and metrics
│   └── visualisations.py     # Stage 4: Generates all charts
├── Graphs/                   # Output PNG charts
├── notebooks/
│   └── workflow_and_dashboard.ipynb  # End-to-end pipeline walkthrough
├── requirements.txt
└── README.md
```

---

## Pipeline Overview

```
Stage 1              Stage 2                  Stage 3           Stage 4
DATA ACQUISITION  >  LOADING & ENGINEERING  >  ANALYSIS      >  VISUALISATION
pre_data_loading.py  data_loading.py           analysis.py       visualisations.py
       |                    |                      |                    |
       v                    v                      v                    v
data/Raw/*.csv      data/Processed/          Console stats       Graphs/*.png
                    flights.csv/.json
```

| Stage | Script | Input | Output |
|-------|--------|-------|--------|
| 1. Data Acquisition | `pre_data_loading.py` | GitHub (nycflights13) | `data/Raw/*.csv` |
| 2. Loading & Engineering | `data_loading.py` | `data/Raw/*.csv` | `data/Processed/flights.csv` |
| 3. Statistical Analysis | `analysis.py` | `data/Processed/flights.csv` | Console output |
| 4. Visualisation | `visualisations.py` | `data/Processed/flights.csv` | `Graphs/*.png` |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-team/flight-analysis.git
cd flight-analysis
```

### 2. Install dependencies

Requires **Python 3.8+**. Then run:

```bash
pip install -r requirements.txt
```

### 3. Run the pipeline

Run the scripts in order from the project root:

```bash
# Stage 1 – Download raw CSVs from GitHub
python src/pre_data_loading.py
# Output: data/Raw/

# Stage 2 – Merge, clean, and engineer features
python src/data_loading.py
# Output: data/Processed/

# Stage 3 – Run statistical analysis
python src/analysis.py
# Output: printed metrics to console

# Stage 4 – Generate visualisations
python src/visualisations.py
# Output: Graphs/
```

All scripts must be run from the project root directory.

Alternatively, the full pipeline can be run interactively in one place via the Jupyter notebook:

```bash
jupyter notebook notebooks/workflow_and_dashboard.ipynb
```

---

## Data Description

336,776 flights from January to December 2013, merged with four companion datasets after loading.

| Column | Description |
|--------|-------------|
| `year`, `month`, `day` | Flight date |
| `dep_time`, `arr_time` | Actual departure and arrival times |
| `dep_delay`, `arr_delay` | Delay in minutes (positive = late, negative = early) |
| `carrier` | Airline code (e.g. `UA` = United, `AA` = American) |
| `origin`, `dest` | Airport codes |
| `distance` | Flight distance in miles |
| `time_of_day` | Engineered feature: Morning, Afternoon, Evening, or Night |
| `is_delayed_departure` | Engineered flag: 1 if departure delay exceeds 15 minutes |
| `weather_risk_score` | Engineered score: normalised wind and precipitation risk (0–1) |

**Note on missing values:** Rows with missing `dep_time` or `arr_time` are treated as cancelled flights and dropped during cleaning. To analyse cancellations separately, retain these rows before running the analysis script.

---

## Key Analyses

- **Average delay per carrier** – which airlines tend to run late?
- **Delay distributions** – spread and consistency of delays per airline
- **Delay by time of day** – are early morning flights more punctual?
- **Seasonal and hourly trends** – how delays vary across months and hours
- **Busiest routes** – most frequent origin-destination pairs
- **Distance vs. delay** – does flight distance affect arrival delay?
- **Outlier detection** – IQR method flags approximately 11% of flights as delay outliers

See `src/analysis.py` for all computed metrics.

---

## Visualisations

All plots are saved as `.png` files in `Graphs/`.

| Chart | File | Description |
|-------|------|-------------|
| Bar chart | `Avg_Carrier_Delays.png` | Average departure delay per carrier, sorted ascending |
| Boxplot | `Carrier_Delay_Distribution.png` | Delay spread and IQR per airline |
| Heatmap | `Delay_Using_A_Heatmap.png` | Average delay by hour of day and month |
| Scatter plot | `FlightDistance_vs_FlightDelay.png` | Flight distance vs arrival delay |
| Bar chart | `Top_Ten_Routes.png` | Top 10 busiest NYC routes by flight count |

---

## Error Handling and Data Validation

- Missing critical fields (`dep_time`, `arr_time`, `carrier`, `origin`, `dest`) are detected and rows dropped with a printed count
- Duplicate rows are removed after merging
- Column types are coerced after merge to ensure numeric operations work correctly
- NumPy `np.clip()` is used to bound the weather risk score within [0, 1]
- All file paths are checked with `os.path.exists()` before download to avoid overwriting

---

## Code Quality

- Follows PEP 8 style guidelines throughout
- All functions include docstrings describing purpose, parameters, and return values
- Complex logic (vectorised operations, IQR detection, feature engineering) is annotated with inline comments
- Functions are modular and single-purpose (e.g. `merge_companion_data()`, `clean_data()`, `engineer_features()`)

---

## Dependencies

Listed in `requirements.txt`:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `requests`
- `jupyter`

Install with:

```bash
pip install -r requirements.txt
```

---
