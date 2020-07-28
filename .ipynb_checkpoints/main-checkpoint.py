import pandas as pd
import numpy as np

df = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv')

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']
           

df.drop(columns=to_drop, inplace=True, axis=1)
df['Identifier'].is_unique
print(df.head())
