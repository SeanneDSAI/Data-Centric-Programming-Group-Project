# Data-Centric-Programming-Group-Project

Flight Delay Analysis – NYC 2013
This project explores flight delays from New York City airports (JFK, LGA, EWR) in 2013. We look at which airlines are most delayed, how delays vary by time of day and month, and what routes are busiest. The data comes from the nycflights13 dataset (or similar).

Team Members & Roles
Dillon – Data Engineer
Responsible for loading and cleaning the data, handling missing values, and preparing the dataset for analysis.

Jack – Data Analyst
Does the number crunching: calculates average delays, finds patterns, and extracts insights from the data.

Ollu – Visualization Lead
Creates clear charts and graphs to show what the numbers mean.

Seanne – Documentation Lead
Keeps the README up to date, manages the repo, and makes sure everything is easy to understand.

How to Run the Project
Clone the repository
git clone https://github.com/your-team/flight-analysis.git

Install dependencies
Make sure you have Python 3.8+ installed. Then run:
pip install -r requirements.txt

Run the pipeline

First, run the data loader:
python src/data_loading.py
This reads the raw CSV and saves a cleaned version in data/processed/.

Then run the analysis:
python src/analysis.py
This will compute various statistics and may save intermediate results.

Finally, run the visualizations:
python src/visualization.py
Plots will be saved in outputs/figures/.

All scripts are designed to be run from the project root.

Data Description
We have about 336,000 flights from January to December 2013. The key columns are:

year, month, day – flight date

dep_time, arr_time – actual departure/arrival times

dep_delay, arr_delay – delays in minutes (positive means late)

carrier – airline code (e.g., UA for United, AA for American)

origin, dest – airport codes

distance – flight distance in miles

Missing values in dep_time or arr_time usually indicate cancelled flights; we handle them by dropping those rows (or you can keep them if you want to analyze cancellations separately).

Key Analyses
Average delay per carrier – which airlines tend to be late?

Delay by time of day – are early morning flights more on time?

Seasonal trends – do delays get worse in winter?

Busiest routes – the most frequent origin-destination pairs.

Correlation between distance and delay – longer flights might have more accumulated delay.

Check the analysis.py script for all the calculated metrics.

Visualizations
Ollu created several plots that illustrate the findings:

Bar chart of average delay per carrier

Boxplot of delay distribution for each airline

Heatmap of delay by hour of day and day of week

Scatter plot of distance vs. delay

Bar chart of top 10 busiest routes

All figures are saved as PNG files in outputs/figures/. You can preview them there.

Dependencies
Python 3.8+

pandas

numpy

seaborn

matplotlib

These are listed in requirements.txt. Install them with pip install -r requirements.txt.

Notes
We assumed that flights with missing dep_time are cancelled and removed them to focus on actual departures.

The cleaned data is stored in data/processed/ so you don’t have to re‑run the loader each time.

If you have any questions, open an issue on GitHub or contact one of the team members.

Enjoy exploring the delays! ✈️