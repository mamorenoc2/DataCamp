import pandas as pd
import numpy as np


taxi_owners = pd.read_pickle('Datasets/Chicago/taxi_owners.p')
taxi_veh = pd.read_pickle('Datasets/Chicago/taxi_vehicles.p')

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the column names of the taxi_own_veh
#print(taxi_own_veh.columns)


#One-to-many merge

licences = pd.read_pickle('Datasets/Chicago/licenses.p')
biz_owners = pd.read_pickle('Datasets/Chicago/business_owners.p')

# Merge the licenses and biz_owners table on account
licenses_owners = licences.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by='account', ascending=False)   

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

