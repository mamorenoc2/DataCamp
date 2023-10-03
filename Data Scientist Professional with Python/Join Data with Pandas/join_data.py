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
zip_demo = pd.read_pickle('Datasets/Chicago/zip_demo.p')

# Merge the licenses and biz_owners table on account
licenses_owners = licences.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by='account', ascending=False)   

# Use .head() method to print the first few rows of sorted_df
#print(sorted_df.head())

cal = pd.read_pickle('Datasets/CTA/cta_calendar.p')
ridership = pd.read_pickle('Datasets/CTA/cta_ridership.p')
stations = pd.read_pickle('Datasets/CTA/stations.p')

#Your goal is to find the total number of rides provided to passengers passing
# through the Wilson station (station_name == 'Wilson') when riding Chicago's 
# public transportation system on weekdays (day_type == 'Weekday') 
# in July (month == 7)

ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
                                    .merge(stations, on='station_id')

filter_criteria = ((ridership_cal_stations['month'] == 7) 
                    & (ridership_cal_stations['day_type'] == 'Weekday') 
                    & (ridership_cal_stations['station_name'] == 'Wilson'))

#print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

#In this exercise, assume that you are looking to start a business in the city 
# of Chicago. Your perfect idea is to start a company that uses goats to mow the 
# lawn for other businesses. However, you have to choose a location in the city 
# to put your goat farm. You need a location with a great deal of space and relatively 
# few businesses and people around to avoid complaints about the smell. 
# You will need to merge three tables to help you choose your location. 
# The land_use table has info on the percentage of vacant land by city ward. 
# The census table has population by ward, and the licenses table lists businesses by ward.

land_use = pd.read_pickle('Datasets/Chicago/land_use.p')
census = pd.read_pickle('Datasets/Chicago/census.p')

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                        .merge(licences, on='ward', suffixes=('_cen', '_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant','account','pop_2010'],ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())
