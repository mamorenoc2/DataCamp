import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
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
The .agg() method allows you to apply your own custom functions to a DataFrame

df[['column_1', 'colunm_2']].agg([function_1, function_2])
'''
'''
In the custom function for this exercise, "IQR" is short for inter-quartile range, which is the 75th percentile 
minus the 25th percentile. It's an alternative to standard deviation that is helpful if your data contains outliers.
'''
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
#print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median]))


# CUMULATIVE STATISTICS
# Sort sales_1_1 by date
sales_1_1 = sales[(sales['department'] == 1) & (sales['store'] == 1)]
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# # Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# # See the columns you calculated
#print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# DROPPING DUPLICATES

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
#print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
#print(holiday_dates.head())

# Count the number of stores of each type
store_counts = store_types.value_counts(subset='type')
#print(store_counts)

# Get the proportion of stores of each type
store_props = store_types.value_counts(subset='type', normalize=True)
#print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts.value_counts(subset='department', sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts.value_counts(subset='department', sort=True, normalize=True)
#print(dept_props_sorted)