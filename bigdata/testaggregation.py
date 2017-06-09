import numpy as np
import pandas as pd

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names, births))
print(BabyDataSet)

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
print(df)

# df.to_csv('births1880.csv', index=False, header=True)
#
# df = pd.read_csv('births1880.csv')
# print(df)
#
# df = pd.read_csv('births1880.csv', names=['Names', 'Births'])
# print(df)

#To find the most popular name or the baby name with the higest birth rate, we can do one of the following
# Method 1:
Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted.head(1))

# Method 2:
print(df['Births'].max())

df['Births'].plot()