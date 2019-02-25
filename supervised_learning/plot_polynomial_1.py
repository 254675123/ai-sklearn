from sklearn.linear_model import Perceptron
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = X[:, 0] ^ X[:, 1]

clf = PolynomialFeatures(interaction_only=True)
X_1 = clf.fit_transform(X)
X_2 = X_1.astype(int)
#X_1 = PolynomialFeatures(interaction_only=True).fit_transform(X).astype(int)

clf = Perceptron(fit_intercept=False, max_iter=10, tol=None, shuffle=False).fit(X_2, y)

res = clf.predict(X_2)
score = clf.score(X_2, y)
print('over')