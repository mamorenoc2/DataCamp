import pandas as pd

homelessness = pd.read_csv("Datasets/homelessness.csv")

#SORTING
homelessness_reg = homelessness.sort_values('region')
homelessness_state = homelessness.sort_values('state')
homelessness_ind = homelessness.sort_values('individuals')
homelessness_fm = homelessness.sort_values('family_members', ascending=False)

#SUBSETTING
regions = homelessness['region']
state = homelessness['state']
individuals = homelessness['individuals']
family_members = homelessness['family_members']
state_populations = homelessness['state_pop']

regions_and_state = homelessness[['region', 'state']]
individuals_gt_10k = homelessness[homelessness['individuals'] > 10000]

#NEW COLUMNS
individuals_gt_10k['new_index'] = range(1, len(individuals_gt_10k) + 1) 



print(homelessness.head())