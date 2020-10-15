import numpy
import pandas
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


data = pandas.read_csv('svmdata2.csv')

train, test = train_test_split(data, test_size=0.2)
train, validation = train_test_split(train, test_size=0.2)

# Bakhshe avval

plot.figure()
plot.scatter(train.iloc[:, 0], train.iloc[:, 1], c=train.iloc[:, 2])
plot.colorbar()
plot.show()


# Bakhshe dovvom

def circTransform(data):
    newData = data[:, :-1]
    newData = numpy.square(newData)
    transform = numpy.array([1, 1])
    return numpy.column_stack((numpy.matmul(newData, transform), data[:, -1]))

transformTrain = circTransform(train.values)
transformTest = circTransform(test.values)

plot.scatter(transformTrain[:, 0], transformTrain[:, 1], c=transformTrain[:, 1])
plot.show()

# Bakhshe sevvom

clf = svm.SVC()
clf = clf.fit(train.iloc[:, 0:1], train.iloc[:, 2])
prediction = clf.predict(test.iloc[:, 0:1])
print(accuracy_score(prediction, test.iloc[:, 2]))

# Bakhshe Chaharom

clf2 = svm.SVC()
clf2.fit(transformTrain[:, :-1], transformTrain[:, -1])
prediction = clf2.predict(transformTest[:, :-1])
print(accuracy_score(prediction, transformTest[:, -1]))
