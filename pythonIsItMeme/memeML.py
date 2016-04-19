import scikit import tree

#Features are weight and bumbpiness
#features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# Corresponding labels (apple or orange) for the weights
#labels = [0, 0, 1, 1]

#Using a decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#Print the result!
print clf.predict([[150, 0]])
