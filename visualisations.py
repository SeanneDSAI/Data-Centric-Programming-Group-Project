import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#loading the dataset
df = pd.read_csv('flights.csv')



#Visualisations 

#Average delay per carrier
plt.figure(figsize=(10, 5))
