import pandas as pd

base_url = "https://raw.githubusercontent.com/tidyverse/nycflights13/main/data-raw/"

tables = ['airlines', 'airports', 'weather', 'planes']

for table in tables:
    df = pd.read_csv(f"{base_url}{table}.csv")
    df.to_csv(f"data/Raw/{table}.csv", index=False)
    print(f"Saved {table}.csv")