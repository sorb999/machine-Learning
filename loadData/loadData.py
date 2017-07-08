# Load dataset
import pandas

# herw we are loading iris data set
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# assigin the header names
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
# print array
print(dataset)
# print keys ie header names
print("keys i.e. Header names:")
print(dataset.keys())