import pandas as pd
import numpy as np


taxi_owners = pd.read_pickle('Datasets/Chicago/taxi_owners.p')
taxi_veh = pd.read_pickle('Datasets/Chicago/taxi_vehicles.p')

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_ward','_cen'))

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)
