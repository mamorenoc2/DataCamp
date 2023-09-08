import pandas as pd
import numpy as np

sales = pd.read_csv('Datasets/sales_subset.csv')

# Print the head of the sales DataFrame
#print(sales.head())

# Print the info about the sales DataFrame
#print(sales.info())

# Print the mean of weekly_sales
#print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
#print(sales['weekly_sales'].median())

# Print the maximum of the date column
#print(sales['date'].max())

# Print the minimum of the date column
#print(sales['date'].min())

'''
The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions 
to more than one column of a DataFrame at once, making your aggregations super-efficient. For example,

df['column'].agg(function)
'''
'''
In the custom function for this exercise, "IQR" is short for inter-quartile range, which is the 75th percentile 
minus the 25th percentile. It's an alternative to standard deviation that is helpful if your data contains outliers.
'''
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median]))