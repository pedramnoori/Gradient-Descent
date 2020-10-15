from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plot
from matplotlib import colors
import numpy
import pandas


data = pandas.read_csv('svmdata.csv')

# Bakhshe avval

train, test = train_test_split(data, test_size=0.3)
train, validation = train_test_split(train, test_size=0.3)
plot.scatter(train.iloc[:, 0], train.iloc[:, 1], c=train.iloc[:, 2], label='asd')
plot.colorbar()
plot.show()


# Bakhshe dovvom

hyper = [0.1, 1, 10, 100, 1000]
acc = []
best_h = -1
for h in hyper:
    clf = svm.SVC(C=h, gamma='auto')
    clf = clf.fit(train.iloc[:, 0:1], train.iloc[:, 2])
    x = clf.predict(validation.iloc[:, 0:1])
    new_acc = accuracy_score(validation.iloc[:, 2], x)
    if new_acc > best_h:
        best_h = new_acc
    acc.append(new_acc)

h_labels = ['0.1', '1', '10', '100', '1000']

plot.scatter(h_labels, acc, label='accuracy')
plot.show()


# Bakhshe sevvom

clf = svm.SVC(C=best_h)
clf.fit(train.values[:, :-1], train.values[:, -1])

class_1 = train.values[train.values[:, -1] == -1]
class_2 = train.values[train.values[:, -1] == 1]

x_min = min(min(class_1[:, 0]), min(class_2[:, 0]))
x_min = x_min - 0.5
x_max = max(max(class_1[:, 0]), max(class_2[:, 0]))
x_max = x_max + 0.5
y_min = min(min(class_1[:, 1]), min(class_2[:, 1]))
y_min = y_min - 0.5
y_max = max(max(class_1[:, 1]), max(class_2[:, 1]))
y_max = y_max + 0.5

bound = [-1, 0, 1]
color = colors.ListedColormap(['b', 'r'])
norms = colors.BoundaryNorm(bound, color.N)

x_x, y_y = numpy.meshgrid(numpy.arange(x_min, x_max, 0.1), numpy.arange(y_min, y_max, 0.1))
pre = clf.predict(numpy.c_[x_x.ravel(), y_y.ravel()])
pre = pre.reshape(x_x.shape)
plot.contourf(x_x, y_y, pre, cmap=color, norm=norms, alpha=0.35)

plot.scatter(class_1[:, 0], class_1[:, 1], color='blue', label='-1')
plot.scatter(class_2[:, 0], class_2[:, 1], color='red', label='1')
plot.legend()
plot.show()
