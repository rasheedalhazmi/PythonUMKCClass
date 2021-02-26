import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('restaurant.csv')
#Skew of the target
print(train.revenue.skew())
plt.hist(train.revenue)
plt.show()



##handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
#Wrangling the non-numric features
#cat = train.select_dtypes(exclude=[np.number])
#print(cat.describe())
#print(train.Type.value_counts())

##Top Five
numricfear = train.select_dtypes(include=[np.number])
corr = numricfear.corr()
print(corr['revenue'].sort_values(ascending=False)[:5], '\n')
print(corr['revenue'].sort_values(ascending=False)[-5:])
##Build a linear model
y = np.log(train.revenue)
X = data.drop(['revenue', 'Id'], axis=1)

#log transform the target
print('skew is ', y.skew())
plt.hist(y)
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
##Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

