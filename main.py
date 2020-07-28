import pandas as pd

df=pd.read_csv('Datasets/owid-covid-data.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

filter=df[['location', 'date', 'new_cases']]

deletedRows=filter[(filter['location'] == 'China') | (filter['location'] == 'Italy') | (filter['location'] == 'South Korea') | (filter['location'] == 'United States')]

#print(

deletedRows.to_csv('output.csv', index=False)
