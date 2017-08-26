import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
print('iris.data.shape')
print(iris.data.shape)
print('iris.target.shape')
print(iris.target.shape)


X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.6, random_state=0)
# X_train = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

print('X_train Data shape')
print(X_train.shape)
print('X_train Data')
print(X_train)

# , y_train.shape

# X_test.shape, y_test.shape


# clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
# clf.score(X_test, y_test)  