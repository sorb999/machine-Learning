
# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)

print('myarray:')
print(myarray)

print('rownames:')
print(rownames)

print('colnames:')
print(colnames)

print('mydataframe:')
print(mydataframe)


print('return first	2 rows:')

rows = mydataframe.head(2);
print(rows)