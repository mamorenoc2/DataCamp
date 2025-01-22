import pandas as pd

homelessness = pd.read_csv("Datasets/homelessness.csv")


#SORTING
'''
    In cases where rows have the same value (this is common if you sort on a categorical variable), you may wish to break the ties by sorting on another column. You can sort on multiple columns in this way by passing a list of column names.
        
        Sort on …	        Syntax
        one column	        df.sort_values("breed")
        multiple columns	df.sort_values(["breed", "weight_kg"])

'''
homelessness_reg = homelessness.sort_values('region')
homelessness_state = homelessness.sort_values('state')
homelessness_ind = homelessness.sort_values('individuals')
homelessness_fm = homelessness.sort_values('family_members', ascending=False)

#SUBSETTING
'''
    When working with data, you may not need all of the variables in your dataset. Square brackets ([]) can be used to select only the columns that matter to you in an order that makes sense to you 
'''
regions = homelessness['region']
state = homelessness['state']
individuals = homelessness['individuals']
family_members = homelessness['family_members']
state_populations = homelessness['state_pop']
regions_and_state = homelessness[['region', 'state']]

#SUBSETTING ROWS
'''
    One of the simplest techniques for this is to find a subset of rows that match some criteria. This is sometimes known as filtering rows or selecting rows.
    There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return True or False for each row, then pass that inside square brackets.
            dogs[dogs["height_cm"] > 60]
            dogs[dogs["color"] == "tan"]
'''                             
individuals_gt_10k = homelessness[homelessness['individuals'] > 10000]
fam_lt_1k_pac = homelessness[(homelessness['family_members'] > 1000) & (homelessness['region'] == 'Pacific')]
#SUBSETTING ROWS with variables
'''
    
'''
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]
# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

#NEW COLUMNS
individuals_gt_10k_2 = individuals_gt_10k.copy()
individuals_gt_10k_2.loc[:, 'new_index'] = list(range(1, len(individuals_gt_10k_2) + 1))

