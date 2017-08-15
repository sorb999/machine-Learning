# Scatter Plot Matrix
import matplotlib.pyplot as plt
import pandas
import pdb

from pandas.tools.plotting import scatter_matrix

url = "https://goo.gl/vhm1eU"

pdb.set_trace()
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
scatter_matrix(data)
plt.show()

