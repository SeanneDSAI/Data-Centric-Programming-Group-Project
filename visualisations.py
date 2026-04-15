import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#loading the dataset
df = pd.read_csv('flights.csv')

#cleaning the 'arr_delay' column
df = df.dropna(subset=[ 'arr_delay'])

#Visualisations 

#Average delay per carrier
plt.figure(figsize=(10, 5))
