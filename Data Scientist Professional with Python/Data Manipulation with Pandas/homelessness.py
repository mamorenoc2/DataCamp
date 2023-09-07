import pandas as pd

homelessness = pd.read_csv("Datasets/homelessness.csv")

#SORTING
homelessness_reg = homelessness.sort_values('region')
homelessness_state = homelessness.sort_values('state')
homelessness_ind = homelessness.sort_values('individuals')
homelessness_fm = homelessness.sort_values('family_members', ascending=False)

print(homelessness_fm.head(10))