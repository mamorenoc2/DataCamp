import pandas as pd
import numpy as np

temperatures = pd.read_csv('Datasets/temperatures.csv')

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')
#print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
#print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
#print(temperatures_ind.reset_index(drop=True))


#SUBSETTING 
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
#print(temperatures[temperatures['city'].isin(cities)])

#with loc
#print(temperatures_ind.loc[cities])

#MULTIPLE INDEX
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

#SLICING
#pandas is loaded as pd. temperatures_ind has country and city in the index, and is available.
temperatures_ind_2 = temperatures.set_index(['country', 'city'])

temperatures_srt = temperatures_ind_2.sort_index()

# Subset rows from Pakistan to Russia
#print(temperatures_srt.loc['Pakistan' : 'Russia'])

# Try to subset rows from Lahore to Moscow
#print(temperatures_srt.loc['Lahore' : 'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
#print(temperatures_srt.loc[('Pakistan', 'Lahore'): ('Russia','Moscow')])

# Subset rows from India, Hyderabad to Iraq, Baghdad
#print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
#print(temperatures_srt.loc[:,'date':'avg_temp_c' ])

# Subset in both directions at once
#   print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq','Baghdad'), 'date': 'avg_temp_c'])

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08':'2011-02'])


# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values='avg_temp_c', index=['country', 'city'], columns = 'year')

# See the result
print(temp_by_country_city_vs_year)