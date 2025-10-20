import pandas as pd
import numpy as np


taxi_owners = pd.read_pickle('Datasets/Chicago/taxi_owners.p')
taxi_veh = pd.read_pickle('Datasets/Chicago/taxi_vehicles.p')
census = pd.read_pickle('Datasets/Chicago/census.p')
wards = pd.read_pickle('Datasets/Chicago/ward.p')


# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

'''
Tipo de JOIN	Qué devuelve
INNER JOIN	Solo coincidencias entre ambas tablas
LEFT JOIN	Todo de la izquierda + coincidencias
RIGHT JOIN	Todo de la derecha + coincidencias
FULL JOIN	Todo de ambas, coincidan o no
CROSS JOIN	Todas las combinaciones posibles
'''

wards_census = wards.merge(census, on='ward')