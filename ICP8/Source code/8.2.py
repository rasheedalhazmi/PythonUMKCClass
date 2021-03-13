import numpy as np
import pandas as pd
from keras.layers.core import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("breastcancer.csv")

mapping = {'B': 1, 'M': 0}
dataset = dataset.replace({'diagnosis': mapping})

dataset = dataset.drop(columns=['id'])
print(dataset.head())

dataset = dataset.values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 1:], dataset[:, 0], test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential()  # create model

my_first_nn.add(Dense(20, input_dim=31, activation='relu'))  # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, initial_epoch=0)
print("-" * 40)
print(my_first_nn.summary())
print("-" * 40)
print(my_first_nn.evaluate(X_test, Y_test))