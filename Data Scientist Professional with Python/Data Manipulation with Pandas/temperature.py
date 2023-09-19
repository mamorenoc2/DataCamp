import pandas as pd
import numpy as np

temperatures = pd.read_csv('Datasets/temperatures.csv')

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
#print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
#print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
#print(temperatures[temperatures['city'].isin(cities)])

#with loc
#print(temperatures_ind.loc[cities])

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

#print(temperatures_ind.loc[rows_to_keep])
# Subset for rows to keep

# Sort temperatures_ind by index values
#print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
#print(temperatures_ind.sort_index(level = ['city']))

# Sort temperatures_ind by country then descending city
#print(temperatures_ind.sort_index(level = ['country', 'city'],  ascending=[True, False]))