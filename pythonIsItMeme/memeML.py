import nltk
from textblob.classifiers import NaiveBayesClassifier

#Utf 8 support
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

print "Welcom 2 meme guesser!"

print "Plz wait we is being loaded..."

#Our testing data features
memeFeatures = []
noMemeFeatures = []

#Read in our meme training data
memeTrainList = [];
with open('trainingDataMeme', 'r') as f:
    for line in f:
        line = line.strip().lower()
        memeTrainList.append([line, 'meme'])

#Add the memes to the features
memeFeatures.extend(memeTrainList)

#Read in our non-meme training data
noMemeTrainList = [];
with open('trainingDataNoMeme', 'r') as f:
    for line in f:
        line = line.strip().lower()
        noMemeTrainList.append([line, 'nomeme'])

#Add the nomemes to the features
noMemeFeatures.extend(noMemeTrainList)

#Train a classifier iteratively, and use the most accurate
maxSize = 0;
if len(memeFeatures) > len(noMemeFeatures):
    maxSize = len(noMemeFeatures)
else:
    maxSize = len(memeFeatures)

#Make sure maxsize is greater than 10
if maxSize > 10:
    print "plz add some moar memes, need moar than 10 ;)"

#Find our index for 10 iterations
featureIteration = len(maxSize) / 10

#Create our features array, and classifiers
classifierFeatures = []
trainedClassifiers = []

for i in range(0, featureIteration):

    #Extend the needed features
    classifierFeatures.extend(memeFeatures[(i * featureIteration): ((i + 1) * featureIteration)])
    classifierFeatures.extend(noMemeFeatures[(i * featureIteration): ((i + 1) * featureIteration)])

    #Train a classifier to be added to our array
    trainedClassifiers.extend(NaiveBayesClassifier(classifierFeatures))

#Next find the most accurate classifier
#Find our accuracy
testingAccuracy = [];
with open('testingData', 'r') as f:
    for line in f:
        line = line.strip().lower()
        testingAccuracy.append([line.split('%')[0], line.split('%')[1]])

#Set the classifier to the first classifier
bClassifier = trainedClassifiers[0]

for i in range(1, len(trainedClassifiers)):
    if trainedClassifiers[i].accuracy(testingAccuracy) < bClassifier.accuracy(testingAccuracy):
        bClassifier = trainedClassifiers[i]

#Times 100 for percent, print our accuracy
print("Meme Accuracy: " + str(bClassifier.accuracy(testingAccuracy) * 100) + "%")


#Read in our testing
testingList = [];
with open('testingData', 'r') as f:
    for line in f:
        line = line.strip().lower()
        testingList.append(line.split('%')[0])

#Print our testing data
for i in range(0, len(testingList)):
    print testingList[i] + " - this haz " + bClassifier.classify(testingList[i])

#Show our most informative features
bClassifier.show_informative_features(15)
