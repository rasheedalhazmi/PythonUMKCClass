import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
train = pd.read_csv('houses.csv')
garage_df = train.get('GarageArea')
print('\n')

plt.scatter(train.get('GarageArea'), train.get('SalePrice'), color='b')
plt.ylabel('Sale Price')
plt.xlabel('Garage Area')
plt.title('OLD')
plt.show()

zScore = np.abs(stats.zscore(garage_df))
print(zScore)
print('\n')
outliers = []
ToBeDropped = []

for i, score in enumerate(zScore):
    if score > 2:
        outliers.append((i, score))
        ToBeDropped.append(i)
        print(i, score)
print(outliers)
print('\n')

train.drop(train.index[ToBeDropped], inplace=True)

plt.scatter(train.get('GarageArea'), train.get('SalePrice'), color='r')
plt.ylabel('Sale Price')
plt.xlabel('Garage Area')
plt.title('New')
plt.show()
print(train.SalePrice.describe())