import numpy as np

X = np.random.randint(1, 20, 20)
print(X, '\n')
print("----------------\n")

a2 = X.reshape((4, 5))
print(a2)
print("----------------\n")

y = a2
y[np.arange(len(a2)), a2.argmax(1)] = 0


print(y)

