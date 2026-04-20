import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#loading the dataset
df = pd.read_csv('flights.csv')



#Visualisations 

#First Visualisation: Average delay per carrier
plt.figure(figsize=(10, 5))
avg_delay_by_carrier = df.groupby('carrier')['dep_delay'].mean().sort_values()
sns.barplot(x = avg_delay_by_carrier.index,y = avg_delay_by_carrier.values,palette = 'magma')
plt.title('Average delay per carrier')
plt.xlabel('Carrier')
plt.ylabel('Mintes Late')
plt.show()
plt.savefig('Avg_Carrier_Delays.png')
plt.close()

#Second Visualisation: Delay distribution by airline
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x = 'carrier', y = 'dep_delay',showfliers = False)
plt.title('Delay distribution by airline')
plt.ylim(-50, 400)
plt.yticks(range(0, 401, 50))
plt.xlabel('Carrier')
plt.ylabel('Delay per carrier')
plt.savefig('Carrier_Delay_Distribution.png')
plt.close()

#Third Visualisation: Delay by hour of day and day of week
