from sklearn import tree
from sklearn import svm
from sklearn import ensemble

# Playing around with a small dataset (11) and using different models from Sklearn to 
# see if they predict a different or the same gender (DecisionTree, SVM and RandomForest)

# [height, weight, shoe size]

X = [[181,80,44],[177,70,43],[160,60,38], [154,54,37],
[166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,65,37],
[171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male']

clf1 = tree.DecisionTreeClassifier()
clf2 = svm.SVC()
clf3 = ensemble.RandomForestClassifier()

clf1 = clf1.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)

prediction1 = clf1.predict([[190,70,42]])
prediction2 = clf2.predict([[190,70,42]])
prediction3 = clf3.predict([[190,70,42]])

print(prediction1)
print(prediction2)
print(prediction3)
