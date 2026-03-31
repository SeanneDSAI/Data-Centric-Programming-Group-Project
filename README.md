# ✈️ Flight Delay Analysis – NYC 2013

> Exploring flight delays from New York City airports (JFK, LGA, EWR) across 336,000 flights in 2013.

We investigate which airlines are most delayed, how delays vary by time of day and month, and which routes are busiest — using the `nycflights13` dataset.

---

## 👥 Team Members

| Name | Role | Responsibilities |
|------|------|-----------------|
| **Dillon** | Data Engineer | Loading & cleaning data, handling missing values, preparing the dataset |
| **Jack** | Data Analyst | Calculating average delays, finding patterns, extracting insights |
| **Ollu** | Visualization Lead | Creating charts and graphs to communicate findings |
| **Seanne** | Documentation Lead | Maintaining the README, managing the repo |

---

## 🚀 Getting Started

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

Run the scripts **in order** from the project root:

```bash
# Step 1 – Load and clean the data
python src/data_loading.py
# Output: data/processed/

# Step 2 – Run the analysis
python src/analysis.py
# Output: computed statistics and intermediate results

# Step 3 – Generate visualizations
python src/visualization.py
# Output: outputs/figures/
```

> ⚠️ All scripts must be run from the **project root**.

---

## 📂 Data Description

~336,000 flights from January–December 2013.

| Column | Description |
|--------|-------------|
| `year`, `month`, `day` | Flight date |
| `dep_time`, `arr_time` | Actual departure/arrival times |
| `dep_delay`, `arr_delay` | Delay in minutes (positive = late) |
| `carrier` | Airline code (e.g. `UA` = United, `AA` = American) |
| `origin`, `dest` | Airport codes |
| `distance` | Flight distance in miles |

> **Note on missing values:** Rows with missing `dep_time` or `arr_time` are treated as cancelled flights and dropped. To analyse cancellations separately, keep these rows before running the analysis script.

---

## 🔍 Key Analyses

- **Average delay per carrier** – which airlines tend to run late?
- **Delay by time of day** – are early morning flights more punctual?
- **Seasonal trends** – do delays worsen in winter?
- **Busiest routes** – most frequent origin–destination pairs
- **Distance vs. delay** – do longer flights accumulate more delay?

See [`src/analysis.py`](src/analysis.py) for all computed metrics.

---

## 📊 Visualizations

All plots are saved as `.png` files in `outputs/figures/`.

| Chart | Description |
|-------|-------------|
| Bar chart | Average delay per carrier |
| Boxplot | Delay distribution by airline |
| Heatmap | Delay by hour of day and day of week |
| Scatter plot | Distance vs. delay |
| Bar chart | Top 10 busiest routes |

---

## 📦 Dependencies

Listed in [`requirements.txt`](requirements.txt):

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

Install with:
```bash
pip install -r requirements.txt
```

---

## 📝 Notes

- Cleaned data is saved in `data/processed/` — no need to re-run the loader each time.
- Cancelled flights (missing `dep_time`) are excluded by default to focus on actual departures.
- Questions? Open a [GitHub Issue](../../issues) or reach out to any team member.
