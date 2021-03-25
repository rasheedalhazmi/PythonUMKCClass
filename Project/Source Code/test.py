import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn import datasets
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

dataset = pd.read_csv('Cleaned-Data.csv')
drop_dataset = dataset.drop(['Country'], axis=1)

pca = PCA(2)

# Transform the data
df = pca.fit_transform(drop_dataset)

print(df.shape)

# Initialize the class object
kmeans = KMeans(n_clusters=3)

# predict the labels of clusters.
label = kmeans.fit_predict(df)

print(label)


# filter rows of original data
filtered_label0 = df[label == 0]

# plotting the results
plt.scatter(filtered_label0[:, 0], filtered_label0[:, -1])
plt.show()

#dataset.info()

#print(dataset.Country.value_counts().sum())

#x = dataset.iloc[:]

#drop_dataset = x.drop(['Country'], axis=1)

#km = KMeans(n_clusters=2)
#km.fit(drop_dataset) # predict the cluster for each data point
#y_cluster_kmeans = km.predict(drop_dataset)

#sns.scatterplot(drop_dataset,y_cluster_kmeans)
#plt.show()




#x = dataset.iloc[:]

#y = dataset.iloc[:,-1]

#print(x.shape, y.shape)


#sns.FacetGrid(x=316801, y=27, data=dataset)



"""
print(dataset.sample(10))

print(dataset.describe())

print(dataset.isnull().sum())

drop_dataset = dataset.drop(['Country'], axis=1)


print(drop_dataset)

print(drop_dataset.skew())

target = np.log(drop_dataset)
print('skew', target.skew())
#plt.hist(target)
plt.show()
"""