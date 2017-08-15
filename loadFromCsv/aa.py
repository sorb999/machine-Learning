# # Scatter Plot Matrix
# import matplotlib.pyplot as plt
# import pandas
# from pandas.tools.plotting import scatter_matrix
# names = ['class','zzz']

# data = pandas.read_csv("abc.tra", header=None)
# scatter_matrix(data)
# plt.show()




# Statistical Summary
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class', 'class2']
data = pandas.read_csv(url, names=names)
description = data.describe()
print(description)