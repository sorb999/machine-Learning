from sklearn import datasets
import matplotlib.pyplot as plt 
iris = datasets.load_iris()
data = iris.data

# print(data.shape)
# print(iris.DESCR)

digits = datasets.load_digits()
# print(digits.images)

print('img1')
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r) 
plt.show()
print('img2')
plt.imshow(digits.images[2], cmap=plt.cm.gray_r) 
plt.show()
