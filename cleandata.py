import pandas as pd
import numpy as np

df=pd.read_csv('Datasets/owid-covid-data.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

selectedColumns=df[['location', 'date', 'new_cases']]

selectedRows=selectedColumns[(selectedColumns['location'] == 'China') | (selectedColumns['location'] == 'Italy') | (selectedColumns['location'] == 'South Korea') | (selectedColumns['location'] == 'United States')]

# selectedColumns China data
#chinaData=selectedRows[(selectedRows['location'] == 'China')]

#chinaData = chinaData.rename(columns={'new_cases': 'China'})

#get all values in location
countries = selectedRows.location.unique()

#start loop through the rows
for country in countries:
	selectedCountry = selectedRows[(selectedRows['location'] == country )]
	selectedRows.insert(2, country, '') 
	selectedRows[country] = selectedCountry['new_cases']
	selectedRows = selectedRows.apply(lambda x: pd.Series(x.dropna().values)).fillna('')

#print(selectedCountry['new_cases'].tolist())

del selectedRows['location']
del selectedRows['new_cases']
selectedRows = selectedRows.loc[:selectedRows[selectedRows['date'] == '2019-12-31'].index[1]-1 :] 
#selectedRows = selectedRows.iloc[:row-1]

selectedRows.to_csv('owid-covid-data-cleaned.csv', sep='\t', index=False)
#np.savetxt('owid-covide-data-cleaned.txt', selectedRows, fmt='%s', delimiter='\t')
