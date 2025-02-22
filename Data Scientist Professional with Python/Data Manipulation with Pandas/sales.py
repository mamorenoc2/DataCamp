import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import numpy as np

sales = pd.read_csv('Datasets/sales_subset.csv')

# Print the head of the sales DataFrame
# print('DATAFRAME HEAD \n', sales.head())

# .info() shows information on each of the columns, such as the data type and number of missing values.v
# print('DATAFRAME INFO \n', sales.info())

# .shape returns the number of rows and columns of the Dataframe
# print('DATAFRAME SHAPE', sales.shape)

# .describe() calculates a few summary statistics for each column.
# print('DATAFRAME SUMMARY \n', sales.describe())

# print(sales.values)
# print(sales.columns)
print(sales.index)

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
#print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
#print(holiday_dates.head())

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
#print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
#print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
#print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
#print(dept_props_sorted)


#DIFICULT WAY
# Calc total weekly sales
sales_all = sales['weekly_sales'].agg('sum')

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].agg('sum')

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]['weekly_sales'].agg('sum')

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]['weekly_sales'].agg('sum')

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
#print(sales_propn_by_type)


#EASY WAY
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
#print(sales_by_type_is_holiday.head())

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
#print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])
# Print unemp_fuel_stats
#print(unemp_fuel_stats)

# PIVOTING METHOD
# Pivot tables are the standard way of aggregating data in spreadsheets
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=np.mean)

# Print mean_sales_by_type
#print(mean_sales_by_type)

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=[np.median, np.mean])

# Print mean_med_sales_by_type
#print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales', index='type', columns='is_holiday')

# Print mean_sales_by_type_holiday
#print(mean_sales_by_type_holiday)

# Print mean weekly_sales by department and type; fill missing values with 0
#print(sales.pivot_table(values='weekly_sales', index='type', columns='department', fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
#print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))