import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#loading the dataset
df = pd.read_csv('flights.csv')



#Visualisations 

#First Visualisation: Average delay per carrier
plt.figure(figsize=(12, 6))
avg_delay_by_carrier = df.groupby('carrier')['dep_delay'].mean().sort_values()
sns.barplot(x = avg_delay_by_carrier.index,y = avg_delay_by_carrier.values,hue = avg_delay_by_carrier.index,palette = 'magma',legend = False)
plt.title('Average delay per carrier')
plt.xlabel('Carrier')
plt.ylabel('Minutes Late')
plt.savefig('Avg_Carrier_Delays.png')
plt.close()

#Second Visualisation: Delay distribution by airline
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x = 'carrier', y = 'dep_delay',showfliers = False)
#showfliers is used above to remove outliers due to extremes which can cause the boxplots to be out of focus
plt.title('Delay distribution by airline')
plt.ylim(-50, 400)
plt.yticks(range(0, 401, 50))
plt.xlabel('Carrier')
plt.ylabel('Delay per carrier')
plt.savefig('Carrier_Delay_Distribution.png')
plt.close()

#Third Visualisation: Delay by hour of day and day of week
plt.figure(figsize=(12, 6))
#A pivot tbale is needed to show the delay for each hour of every month
pivot_table = df.pivot_table(index='month',columns='hour',values='dep_delay',aggfunc='mean')
sns.heatmap(pivot_table, cmap='Blues')
plt.title('Delay by hour of day and day of week')
plt.xlabel('Hour')
plt.ylabel('Month')
plt.savefig('Delay_Using_A_Heatmap')
plt.close()

#Fourth Visualisations: Distance vs. delay
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='distance', y='arr_delay',alpha = 0.1,color = 'brown')
#The color brown was used to how all the values on the chart 
plt.title('Distance vs. delay')
plt.xlabel('Distance')
plt.ylabel('Delay')
plt.savefig('FlightDistance vs FlightDelay')
plt.close()

#Fifth Visualisation: Top 10 busiest routes
plt.figure(figsize=(14, 6))
df['route'] = df['origin'] + '-' + df['dest']
top_routes = df['route'].value_counts().head(10)
#Using Head(10) gets the first 10 values from  the data frame which is then put in the top_routes variable 
top_routes.plot(kind = 'bar',color = 'blue')
plt.title('Top 10 Busiest Routes')
plt.ylabel('Number of Flights')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Top_Ten_Routes.png')
plt.close()