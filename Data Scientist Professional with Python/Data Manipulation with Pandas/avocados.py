import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

avocados = pd.read_pickle('Datasets/avoplotto.pkl')
# Look at the first few rows of data
#print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar')

# Show the plot
#plt.show()

plt.clf()


# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line')

# Show the plot
#plt.show()
plt.clf()

#Create a scatter plot with nb_sold on the x-axis and avg_price on the y-axis. Title it 
# "Number of avocados sold vs. average price"
avocados.plot(kind='scatter', x='nb_sold', y='avg_price', title='Number of avocados sold vs. average price')
#plt.show()
plt.clf()

# Histogram of conventional avg_price 
avocados[avocados['type'] == 'conventional']['avg_price'].hist(alpha=0.5, bins=20)

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(['conventional', 'organic'])

# Show the plot
#plt.show()
plt.clf()
plt.close()

#MISSING VALUES
# avocados_2016, a subset of avocados that contains only sales from 2016, is available.
avocados_2016 = avocados[avocados['year'] == 2016]

#Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
#plt.show()