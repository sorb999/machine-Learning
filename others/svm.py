from sklearn import datasets, svm
import pdb
# pdb.set_trace()
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target
svc = svm.SVC(C=1, kernel='linear')
aa = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
# bb = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[:-100], y_digits[:-100])
# print(bb)
print(aa)