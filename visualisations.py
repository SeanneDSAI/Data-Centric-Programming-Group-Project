import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('flights.csv')

df = df.dropna(subset=[ 'arr_delay'])

plt.figure(figsize=(10, 5))
